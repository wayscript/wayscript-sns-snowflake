import os

from flask import Flask, request
import snowflake.connector

# configure user snowflake credentials
# The preferred account identifier includes the name of the account along with its organization (e.g. myorg-account123)
# Find this info in your dashboard > Admin ( Left side bar ) > Accounts
# The ORG will be listed at the top above all the accounts
# The account will be the value in the column 'ACCOUNT' for the account you wish to use. 

# Create snowflake client
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

warehouse = ''
database = ''
schema = ''
sql_statement = ''

cur.execute(sql_statement)
df = cur.fetch_pandas_all()
json_response = df.to_json()

print(json_response)
