from flask import Flask, request
import pandas as pd
import boto3

import os 

app = Flask(__name__)

# AWS SETTINGS
# The secret key and access key come from an IAM user
# These secrets should be placed inside the .secrets file and then accessed using os
# For help creating an IAM user with permissions view the AWS docs
# https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

# AWS Resource Calls
# Boto3 is used in this example to access AWS resources
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

# AWS Functions

def create_sns_client():
    client = boto3.client(
    'sns',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )
    return sns_client

def create_s3_client():
    client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )
    return s3_client

SNOWFLAKE_USER = os.environ.get('snowflake_user')
SNOWFLAKE_PASSWORD = os.environ.get('snowflake_password')
SNOWFLAKE_ACCOUNT = os.environ.get('snowflake_account')

def create_snowflake_client():
        USER = os.environ.get('user')
        PASSWORD = os.environ.get('password')
        ACCOUNT = os.environ.get('account')
        conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        )
        cur = conn.cursor()
        return cur


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return 'Please send POST'
    if request.method == 'POST':
        # For subscribing remove comments on these lines
        #webhook_data = request.json.get('data')
        #print(webhook_data)

        s3_client = create_s3_client()
        s3_client.download_file(bucket_name, 'File-name-here.xlsx', 'temp_file.xlsx')

        # Get snowflake data
        cur = create_snowflake_client()

        warehouse = ''
        database = ''
        schema = ''
        sql_statement = ''

        cur.execute(sql_statement)
        df2 = cur.fetch_pandas_all()

        #creates 2 dataframes
        df1 = pd.read_excel('temp_file.xlsx')
        #makes third dataframe of the new additions
        df3 = pd.concat([df1, df2]).drop_duplicates(keep=False)
        print(df3)


        # Snowflake Write statement
        #convert new rows into an SQL statement
        success, nchunks, nrows, _ = write_pandas(cnx, df3, 'customers')

        return {'data':[success, nchunks, nrows]}

if __name__ == '__main__':
    app.run()
    