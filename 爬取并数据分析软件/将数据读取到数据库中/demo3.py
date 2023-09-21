# -*- coding: utf-8 -*-
# time:2023/8/6 15:16
# file demo3.py
# outhor:czy
# email:1060324818@qq.com

import datetime
import pandas as pd
import sqlite3

# Load Excel data starting from the second row
excel_file = '1/amzon_DeerValley.xlsx'
df = pd.read_excel(excel_file, usecols="A:F")  # Specify columns A to F, and skip the first row

# Establish a connection to the SQLite database and create a cursor
db_file = 'amzon_DeerValley.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Insert the data from the DataFrame into the SQLite table
insert_query = '''INSERT INTO data (
                    主图, 目前售价, 上次同步前售价,
                    本次更新review数量, 上次同步时数量,
                    更新时间, 直达的落地页, 产品评分, 商品名称
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''

current_datetime = datetime.datetime.now()
for index, row in df.iterrows():
    data_tuple = (
        row['E'],  # Replace 'A' with the actual column name from your Excel file
        row['C'],  # Replace 'B' with the actual column name from your Excel file
        '',  # Replace 'C' with the actual column name from your Excel file
        row['D'],  # Replace 'D' with the actual column name from your Excel file
        '',  # Replace 'E' with the actual column name from your Excel file
        current_datetime,  # Replace 'F' with the actual column name from your Excel file
        row['A'],  # Dummy value for update_time, as it is not present in the Excel data
        row['B'],  # Dummy value for Direct_landing_page, as it is not present in the Excel data
        row['F'],  # Dummy value for Product_rating, as it is not present in the Excel data
    )
    cursor.execute(insert_query, data_tuple)

# Commit changes and close the connection
conn.commit()
conn.close()
