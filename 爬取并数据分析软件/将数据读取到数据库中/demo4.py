# -*- coding: utf-8 -*-
# time:2023/8/6 15:47
# file demo4.py
# outhor:czy
# email:1060324818@qq.com
import pandas as pd

excel_file = '1/amzon_American_Standard.xlsx'
columns_to_read = ['A', 'B', 'C', 'D', 'E', 'F']
df = pd.read_excel(excel_file, usecols=columns_to_read)

# Print the data in each column
for column in columns_to_read:
    print(f"Data in {column}:")
    print(df[column])
    print("--------------------")
