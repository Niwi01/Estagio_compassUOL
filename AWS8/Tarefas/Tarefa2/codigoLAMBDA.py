import csv
import requests
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Leitura do arquivo CSV da Etapa 1
    csv_file_path = "Raw/Local/CSV/Movies/2023/05/18/movies.csv"  # Defina o caminho correto para o arquivo CSV
    movies = []

    s3 = boto3.client(
        's3', 
        aws_access_key_id='-',
        aws_secret_access_key='-',
        region_name='us-east-1')

    bucket_name = 'data-lake-niwea'

    # Download do arquivo CSV do S3
    s3.download_file(bucket_name, csv_file_path, '/tmp/movies.csv')

    with open('/tmp/movies.csv', "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="|")
        next(reader)  # Pular o cabeçalho do arquivo CSV

        movies_ids = set()
        for row in reader:
            if row[5] == "Adventure":
                movie = {
                    "id": row[0],
                    "TituloPrincipal": row[1],
                    "TituloOriginal": row[2],
                    "anoLancamento": row[3],
                    "tempoMinutos": row[4],
                    "genero": row[5],
                    "notaMedia": float(row[6]),
                    "numeroVotos": int(row[7]),
                }
                
                if movie["id"] not in movies_ids:
                    movies.append(movie)
                    movies_ids.add(movie["id"])

    movies.sort(key=lambda x: x["numeroVotos"])

    groups = [movies[i:i+100] for i in range(0, len(movies), 100)]

    api_key = "1744690f9968eb9fd53a25efe19c58d7"
    url_tmdb = "https://api.themoviedb.org/3"

    def get_movie_details(imdb_id):
        endpoint = f"/find/{imdb_id}"
        url = f"{url_tmdb}{endpoint}?api_key={api_key}&language=en-US&external_source=imdb_id"
        response = requests.get(url)
        data = response.json()
        if "movie_results" in data:
            return data["movie_results"][0] if data["movie_results"] else None
        return None

    for i, group in enumerate(groups):
        selected_movies = group

        for movie in selected_movies:
            imdb_id = movie["id"]
            details = get_movie_details(imdb_id)
            if details:
                movie["tmdb_details"] = details
        
        
        json_file_path = f"/tmp/filminhos_{i+1}.json"
        with open(json_file_path, "w") as json_file:
            json.dump(selected_movies, json_file, indent=4)

        s3.upload_file(json_file_path, bucket_name, f"Raw/TMDB/JSON/{datetime.now().strftime('%Y/%m/%d')}/{json_file_path}")


    return {
        'statusCode': 200,
        'body': 'Data ingestion complete'
    }
