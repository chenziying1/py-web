from tkinter import *
import tkinter.messagebox
import requests
import json

def fanyi_danchi(key):
    base_url = 'https://fanyi.baidu.com/sug'
    data = {'kw': key}
    headers = {
        'content-length': str(len(data)),
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://fanyi.baidu.com/',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.post(base_url, headers=headers, data=data)
    result = ''
    if len(response.json()['data']) == 0:
        text.delete(1.0, END)
        text.insert(INSERT, "提示:请确认输入的语句是否正确")
    else:
        for i in response.json()['data']:
            result += i['v'] + '\n'
        text.delete(1.0, END)
        text.insert(INSERT, key + "的翻译结果为" + result)

def fanyi_juzhi(key):
    base_url = 'https://fanyi.baidu.com/transapi'
    data = {
          'from': 'en',
          'to': 'zh',
          'query': key,
          'source': 'txt'
          }
    keys = len(key.replace(' ',''))
    headers = {
        #'content-length': str(len(data)),
        #应该是这里的原因导致我们翻译不了句子,
              #其实也不是，sug应该是翻译单词，transapi翻译句子
        'content-length': str(keys),
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://fanyi.baidu.com/',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.post(base_url, headers=headers, data=data)
    result = ''
    if len(response.json()['data']) == 0:
        text.delete(1.0, END)
        text.insert(INSERT, "提示:请确认输入的语句是否正确")
    else:
        ans = json.loads(response.text)['data'][0]['dst']
        text.delete(1.0, END)
        text.insert(INSERT, "翻译结果为" + "\n" + ans)
                  
                  
        


 
 
def main():
          password = E1.get()
          if ' ' in password:
                  fanyi_juzhi(password)
          elif ' ' not in password:
                  fanyi_danchi(password)

                  
def helloCallBack():
       E1.delete(0,"end")

root = Tk()                     
root.geometry("500x400+100+50")


E1 = Entry(root, bd =3)
E1.pack(fill="x",padx=10,pady=10)


 
B1 = Button(root, text ="清空输入框", command = helloCallBack,activebackground='red',bg='white')
 
B1.pack(fill="x",padx=10,pady=10)#side=LEFT,

B2 = Button(root, text ="开始翻译", command = main,activebackground='green',bg='white')
 
B2.pack(fill="x",padx=10,pady=10)

text = Text(root)
text.pack(fill="x")

root.mainloop()                 # 进入消息循环
