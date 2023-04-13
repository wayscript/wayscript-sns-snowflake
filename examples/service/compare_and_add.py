import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

# Compare two dataframes to find the differences
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

data2 = {
  "calories": [420, 380],
  "duration": [50, 40]
}

#creates 2 dataframes
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

#makes third dataframe of the new additions
df3 = pd.concat([df1, df2]).drop_duplicates(keep=False)
print(df3)


# Snowflake Write statement
#convert new rows into an SQL statement
success, nchunks, nrows, _ = write_pandas(cnx, df3, 'customers')