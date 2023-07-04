from urllib.request import urlopen

response = urlopen('https://www.baidu.com/')

print('response的类型：',type(response))
print('状态码：',response.status,'响应消息:',response.msg,'http版本:',response.version)
print('响应头:',response.getheaders())
print('cont-type:',response.getheader('Content-Type'))
print(response.read().decode('utf-8'))
