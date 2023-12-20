import logging
import boto3
from botocore.exceptions import ClientError
import os

acesso='AKIATHCDWTGSODP2KXV4'
secreto='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'
regiao='us-east-1'

def upload_file(file_name, bucket, folder_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param folder_name: Folder name in the S3 bucket. If not specified, the file will be uploaded to the bucket root.
    :return: True if file was uploaded, else False
    """

  # If folder_name is specified, append it to the object_name
    if folder_name is not None:
        object_name = os.path.join(folder_name, os.path.basename(file_name))
    else:
        object_name = os.path.basename(file_name)
    
    # Upload the file
    s3_client = boto3.client('s3', aws_access_key_id=acesso, aws_secret_access_key=secreto,region_name=regiao)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

file1 = os.path.abspath('movies.csv')
file2 = os.path.abspath('series.csv')

bucket_name = 'data-lake-niwea'

upload_success1 = upload_file(file1, bucket_name, folder_name='Raw/Local/CSV/Movies/2023/05/18')
upload_success2 = upload_file(file2, bucket_name, folder_name='Raw/Local/CSV/Series/2023/05/18')





