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
        print("提示:请确认输入的单词/词语是否正确")
    else:
        for i in response.json()['data']:
            result += i['v'] + '\n'
        print(key + "的翻译结果为")
        print(result)

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
        print("提示:请确认输入的语句是否正确")
    else:
        ans = json.loads(response.text)['data'][0]['dst']
        print(ans)
        


 
 
def main():
    tf_list = {'yes', '是', '继续','y' }
    tf = True
    while tf:
        password = input("请选择要翻译的类型(1.单词,2.句子):")
        if password == '1':
                  kw = input("请输入要翻译的单词:")
                  fanyi_danchi(kw)
                  new_tf = input("是否继续查询")
                  if new_tf not in tf_list:
                      new_tf = False
                      print("查询结束")
                  else:
                      new_tf = True
        elif password == '2':
                  kw = input("请输入要翻译的句子:")
                  fanyi_juzhi(kw)
                  new_tf = input("是否继续查询")
                  if new_tf not in tf_list:
                      new_tf = False
                      print("查询结束")
                  else:
                      new_tf = True
        tf = new_tf

 
 
if __name__ == '__main__':
    main()
