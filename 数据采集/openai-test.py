# -*- coding: utf-8 -*-
# time:2023/4/26 23:32
# file openai-python链接mysqldemo.py
# outhor:czy
# email:1060324818@qq.com
# 第一个是433 无法连接的问题用http://localhost:7890解决了
# 第二个是api key的问题
import os
import openai

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

