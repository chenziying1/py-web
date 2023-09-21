import pandas as pd
import sqlite3

# Read data from Excel
excel_file = '1/amzon_American_Standard.xlsx'
df = pd.read_excel(excel_file)

# Connect to the database
conn = sqlite3.connect('1/amzon_American_Standard.db')

# Store data in the database (replace 'table_name' with your desired table name)
table_name = 'data'
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the connection
conn.close()
