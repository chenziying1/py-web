# -*- coding: utf-8 -*-
# time:2023/8/3 9:27
# file demo2.py
# outhor:czy
# email:1060324818@qq.com

import sqlite3

def create_database(name):
    # Establish a connection to the database (creates a new database if it doesn't exist)
    conn = sqlite3.connect(name)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_American_Standard (
                        id INTEGER PRIMARY KEY,
                        sku TEXT ,
                        主图 TEXT ,
                        目前售价 TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_Fine_Fixtures (
                        id INTEGER PRIMARY KEY,
                        主图 TEXT ,
                        sku TEXT ,
                        目前售价 TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_HOROW (
                        id INTEGER PRIMARY KEY,
                        主图 TEXT ,
                        sku TEXT ,
                        目前售价 TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_Kohler (
                        id INTEGER PRIMARY KEY,
                        主图 TEXT ,
                        目前售价 TEXT ,
                        sku TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_MOHOME (
                        id INTEGER PRIMARY KEY,
                        主图 TEXT ,
                        目前售价 TEXT ,
                        sku TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_Swiss_Madison (
                        id INTEGER PRIMARY KEY,
                        主图 TEXT ,
                        目前售价 TEXT ,
                        sku TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_TOTO (
                        id INTEGER PRIMARY KEY,
                        主图 TEXT ,
                        目前售价 TEXT ,
                        sku TEXT ,
                        上次同步前售价 TEXT,
                        本次更新review数量 TEXT,
                        上次同步时数量 TEXT,
                        更新时间 TEXT ,
                        直达的落地页 TEXT ,
                        产品评分  TEXT,
                        商品名称 TEXT 
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS amzon_Woodbrige (
                            id INTEGER PRIMARY KEY,
                            主图 TEXT ,
                            目前售价 TEXT ,
                            sku TEXT ,
                            上次同步前售价 TEXT,
                            本次更新review数量 TEXT,
                            上次同步时数量 TEXT,
                            更新时间 TEXT ,
                            直达的落地页 TEXT ,
                            产品评分  TEXT,
                            商品名称 TEXT 
                        )''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def connect_to_database(name):
    # Establish a connection to the existing database
    conn = sqlite3.connect(name)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Example: Fetch data from the table
    cursor.execute("SELECT * FROM amzon_TOTO")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    create_database('amzon.db')
    connect_to_database('amzon.db')

