import boto3

# Configure Secrets from IAM User

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

bucket_name = 'wayscript-tutorials'


## Create Client
def create_s3_client():
        s3_client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
        )
        return s3_client

s3_client = create_s3_client()
response = s3_client.get_object(
        Bucket = bucket_name,
        Key = 's3-snowflake-excel-data.xlsx'
        )

s3_client.download_file(bucket_name, 's3-snowflake-excel-data.xlsx', 'temp_file.xlsx')
