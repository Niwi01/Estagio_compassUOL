create table artista as
SELECT
  ROW_NUMBER() OVER (ORDER BY nomeartista_csv) AS id_artista,
  nomeartista_csv,
  anonascimento_csv,
  anofalecimento_csv,
  profissao_csv
FROM refinando
limit 5