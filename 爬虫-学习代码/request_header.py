from urllib3 import *
import re

http = PoolManager()

url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&clk1=521d93d429fb5641d8c81e1ac867fb77&upsId=521d93d429fb5641d8c81e1ac867fb77'

headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Cookie':'cna=40/8GINjL1sCAX1Unl4pGYqK; cookie2=16d4d33d49eed6f352f1de828889092d; _tb_token_=e7a47eb8aabe; _m_h5_tk=2fecebae02b7a8bb7426cf5c7829f2fe_1658733875149; _m_h5_tk_enc=448b820d9270db3e4434cdfe09095a3d; isg=BG5utnZcgIdoD_aC6JDRtGA2vMQwbzJpo_Ks1Jg353EMew_VAP_ReClyM2eXuCqB; l=eBacHZ6VjC86JVaTBOfZ-urza77O9IObYuPzaNbMiOCP_UfHkS5cB6vegmTMCn1VH6o2R3WaIk_wBMFv2yKInxv9-b293OeK3dC..; tfstk=cKuCBvqys9XCHu8mPkOw4JHzKwzPaYx_6HwZOdfoBV5RGMc3psmNu-twb0X_z7F1.; xlly_s=1'
          }
response = http.request('GET',url,headers = headers)
data = response.data.decode('UTF-8')
print(data)
