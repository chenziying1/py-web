# -*- coding: utf-8 -*-
# time:2023/6/9 9:54
# file tianchong.py
# outhor:czy
# email:1060324818@qq.com


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','richengjilu.settings')

import django
django.setup()
from main.models import message

def populate():
    neirong = [    {   "text":"今天天气真好1!",
            "date":"2023.6.9"
        },
        {   "text": "今天天气真好2!",
            "date": "2023.6.10"
        },
        {   "text": "今天天气真好3!",
            "date": "2023.6.11"
        },
                ]

    for txt in neirong:
        c = add_message(txt["text"],txt["date"])
        for c in message.objects.all():
            print("- {0} -".format(str(c)))

def add_message(text,date):
    c = message.objects.get_or_create(text=text,date=date)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
