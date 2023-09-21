# -*- coding: utf-8 -*-
# time:2023/7/27 21:06
# file homedepot2.py
# outhor:czy
# email:1060324818@qq.com

#<a class="hd-pagination__link " href="/s/DeerValley?Nao=24" aria-label="Next"></a> 最后一页还有这个，但是没有下去的按钮了
#检查有没有这个按钮，有继续，想要爬取就看有没有no_product_elements = soup.select('.results-wrapped--no-products')这个东西不用再循环了
#用在亚马逊上也许可以，这个上完全不行，需要上模拟吗？


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

with open("../资源/cookie.txt", "r", encoding="utf-8") as f:
    a = f.readline()
    a = a.strip()
f.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie':'THD_PERSIST=; THD_CACHE_NAV_PERSIST=; thda.u=243865ae-1789-3550-fcf1-3ae3f47423b6; DELIVERY_ZIP_TYPE=DEFAULT; _pxvid=e307a15e-29f5-11ee-9937-b5137eb47646; _px_f394gi7Fvmc43dfg_user_id=ZTUwN2JkMDAtMjlmNS0xMWVlLTgwM2QtNWRmOGNkNzI0Njlk; QuantumMetricUserID=d5aee330d159889c5737ce0a9f0b1728; ajs_anonymous_id=4b6779ca-5559-419c-ba81-9d64328e83ab; _meta_facebookPixel_beaconFired=1690184672764; _meta_bing_beaconFired=1690184672766; _meta_neustar_mcvisid=19502600107476188242762195511795620360; _meta_movableInk_mi_u=4b6779ca-5559-419c-ba81-9d64328e83ab; _meta_metarouter_timezone_offset=-480; _meta_inMarket_userNdat=C470212DE32BBE64240C7669028A8E16; _meta_amobee_uid=7224529370597234571; _meta_revjet_revjet_vid=5252015208722558780; trx=5252015208722558780; _meta_neustar_fabrickId=E1:f1hVO6EaPo8ojMW0M6qBsgxYtujE2JRRcclNKr_Ge-UKIdYuXE2SXsd8CJSgQsJeBxgyp7JyddNhKWD__EJaXk0gJeyPTaoL5MlG447TPWo; _meta_neustar_tuid=232493304515009662908; _meta_tapAd_id=ae1638ae-755c-4035-b2f9-b8657b8e03dc; THD_NR=1; THD_SESSION=; THD_CACHE_NAV_SESSION=; _meta_acuityAds_auid_failure=failed to make request; _meta_acuityAds_cauid_failure=failed to make request; _meta_yahooMedia_yahoo_id_failure=timeout; _meta_pinterest_derived_epik_failure=timeout; _meta_pinterest_pin-unauth_failure=timeout; aam_uuid=19793098313355285732752287359615775869; _meta_mediaMath_mm_id=e18d645e-1bae-4b00-8b42-c3ae4d3cf61d; _meta_mediaMath_cid=e18d645e-1bae-4b00-8b42-c3ae4d3cf61d; LPVID=M0ZTZiZjJjYzEzZDdlZmY1; x-ttsearch=ca_elasticpecos; _meta_adobe_aam_uuid=19793098313355285732752287359615775869; _meta_googleGtag_ga=GA1.2.2096017905.1690437288; _meta_googleGtag_ga_library_loaded=1690437288667; _meta_adobe_neustar=1690437288678; _meta_adobe_google=1690437288679; _meta_adobe_microsoft=1690437288680; _meta_neustar_aam=19793098313355285732752287359615775869; _meta_adobe_fire={"xandr":false,"revjet":true,"mediaMath":true}; _gcl_au=1.1.442251437.1690437295; _ga=GA1.2.2096017905.1690437288; _gid=GA1.2.1289117859.1690437296; _ga_9H2R4ZXG4J=GS1.1.1690437295.1.1.1690437988.60.0.0; _meta_mediaMath_iframe_counter=5; QSI_SI_2lVW226zFt4dVJ3_intercept=true; HD_DC=origin; AKA_A2=A; akacd_usbeta=3867915947~rv=14~id=c02ecba517783a1a770062822f34ed2d; bm_sz=D65C73C7532CA9293916400567AD8180~YAAQFDIcuBuJrIaJAQAAHZp0lxTaA+AeGcsHIEIZOFhuCw4LyobcM1RYUf8WV81UCeZCjDfWhVzDYVj3FU+3OSe4bnBY0NfuooVNaN8YkYB1lY/gCQdAPhLw69ps6Y/M5E89cONj7wtQ0BTpOpmPMz38mtmznIapbRFDB4TSQz4AcxPnKW0hEcBjOnD34W1csrkU7VzTSATkXAJg6C8mg8l0aNd44Cro+dfMxLnDFRf+awULv+PH+Hv3bm8UUR5ppg2KGxxXgGi+JjgRFEDZdPr5xnoZk3X1iIq1m9Oa7CQioLIESvA=~3158576~3158323; at_check=true; ak_bmsc=9F7DB3F8E31E7817B255CB2AEEBE5A6A~000000000000000000000000000000~YAAQFDIcuHiJrIaJAQAArqp0lxTsjzb+7ea1Tr5ZBJchH7islINuZ5eWmZYtng7yX+ULG1WMi5IYEEt2fEs+Ru5Kw8QTlrRNqWiUkBHBlKr1qGQ2J3BtO1xTtMU5WLeajuVQtGWL9VaJvqNPNt2qkKIiK3LAbvg+oqYn3h6m8hS32RPF+u+HOuZmorajWowuJyd2saS9OqCPTguThMKUCS2wCXzQOugL+Kh2VnBFeqmNzN+L0YTuy/idnSjHmZgvqmg2sKmYGKj3uLs+TMqc8/UZMFpWAmEWq02UjR+8FvIHVZKeRjKtq7GvO+Sm/PRQ05fn9wm6jusFcQNQmpaVI9ONP4eT8XH3n63qUBoNOlxdfm34JIo7fbAXsJwckXwfshwy5j7QAWpat2KuoTR6oLmhKn/Zpv24e47eBR7yfKEUFvVKlBhiqX0Mko3iGc8/pDFB2SQkbyV39q0Si6YheUjgKBdGFy69/2g3QMA8g5q0UrShAECaJn8XpBmOsxs=; thda.s=706fc6b0-0b5c-8f89-fa9a-7a4cfd6731ab; mbox=PC#19688b705bae49689f0c1076193996fa.35_0#1753707964|session#1f5eda69d5ab40f59621c2b3ba076b19#1690465024; THD_LOCALIZER=%7B%22WORKFLOW%22%3A%22LOC_HISTORY_BY_IP%22%2C%22THD_FORCE_LOC%22%3A%221%22%2C%22THD_INTERNAL%22%3A%220%22%2C%22THD_LOCSTORE%22%3A%224702%2BLander%20-%20Seattle%2C%20WA%2B%22%2C%22THD_STRFINDERZIP%22%3A%2298134%22%2C%22THD_STORE_HOURS%22%3A%221%3B7%3A00-20%3A00%3B2%3B6%3A00-21%3A00%3B3%3B6%3A00-21%3A00%3B4%3B6%3A00-21%3A00%3B5%3B6%3A00-21%3A00%3B6%3B6%3A00-21%3A00%3B7%3B6%3A00-21%3A00%22%2C%22THD_STORE_HOURS_EXPIRY%22%3A1690466768%7D; DELIVERY_ZIP=98134; ecrSessionId=868CAEF0AE9D996FE9DE3D29301B2124; AMCVS_F6421253512D2C100A490D45%40AdobeOrg=1; AMCV_F6421253512D2C100A490D45%40AdobeOrg=1585540135%7CMCMID%7C19502600107476188242762195511795620360%7CMCAAMLH-1691067977%7C9%7CMCAAMB-1691067977%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1690470378s%7CNONE%7CMCCIDH%7C240044181%7CvVersion%7C4.4.0; _meta_metarouter_sessionID=1690463178006; thda.m=19502600107476188242762195511795620360; QuantumMetricSessionID=e94edf0933801517e755b27e4cbf91f9; forterToken=e8c67bae9c60499f88e0a882a24c4538_1690463176122__UDF43-mnf-anf_13ck; _abck=5A3B2AAAE8E715FBF77EEC2CC700DACD~-1~YAAQJDIcuH97YHCJAQAA3hx3lwoL27mcxSewEiW0fiI2DYiSE2FBmm1paXdaTbWJNUISa38PrupFzTjO0NvDpAIjlFQb4WZ5DgbBq2J0L8bV5tqjKMy0wR2XnI7GQzhUdhO2X7c6jNouVh1XmIIEhrw/AOJwin1PCv/lKj0JsrapE1Fodg0q/NdmqyaDR1qchDqWoGODuqdqrGuNTgnxsDYaPg0qUPpdqnRm1yzbKoBtpsuZupuRa4K0VN1hPW+jrTkxJY0pGHYskwqRmOx3LFipG7Ue4l2hhSPF3QXcq0H18xw/mhdwST/iTV8Fn2oXNhYvRoEwDIw0tWJ2cCMercLqmAl4iElPCBsDJ+dijrkbWGHvpAWsSFuNNV5W9bWPBPQWc9xY/dLIW6kMLiQH/AdTk4r7hnlutDHd6g==~-1~-1~-1; akavpau_prod=1690463613~id=df39cc50b74778c61c220b40100275ab; s_pers=%20productnum%3D10%7C1693055176299%3B%20s_nr365%3D1690463314179-Repeat%7C1721999314179%3B%20s_dslv%3D1690463314187%7C1785071314187%3B; s_sq=%5B%5BB%5D%5D; s_sess=%20s_cc%3Dtrue%3B%20s_pv_pName%3Dsearch%2520results%253Epagination%3B%20s_pv_pType%3Dsearch%2520results%3B%20s_pv_cmpgn%3D%3B%20s_pv_pVer%3Dplp%253Aversion%253Agen2%3B%20stsh%3D%3B; _px=dcT/5QpTF+KD2k/QfY4WLg6nDgjc+MzK/gLNWvZLZCROHlhk3KVnax3Dw2kZQ/+ff2qNBugJMpCnA3W/i697Mw==:1000:ug8KAkNaI9p+3FiFqLBa7UZv5tmYsacjpcc3acS35kAav4NDsfApIR0erXFJDL+MHH1AZgK2fFvYsWK6O6E4oA4E8nXwJakOPUeXC7qm906nKVhZakH9tQNgyZ1hCxZjJMnQBXgIJ5Xtble2Yztzj/lQR9TepG3XeZnRJBkyEpVWnCkNj66OvApxCXXhfvOGk5HhKlZxi0dC+ZcKMTOuXazUJ8xeOj9PgOsHjQzg06wSZLLkrmmvwStwPb041jjbzvZbqv6TzxZMQlg3Q5ptyA==; _pxde=16273d3a13ed7b1438015cf19d3b819a04c202c0a17ee6c7854254a07fb855d4:eyJ0aW1lc3RhbXAiOjE2OTA0NjM1Njk4Njd9; RT="z=1&dm=www.homedepot.com&si=0ab56f1f-809f-4226-9ffc-b10e3a468bf4&ss=lkl6410v&sl=2&tt=a10&rl=1&nu=4f5l5c7z&cl=3it6&obo=1&ld=eld5&r=4f5l5c7z&ul=eld6"'
}

target_list = ["DeerValley", "TOTO", 'Swiss Madison', 'American Standard', 'Kohler','HOROW','MOHOME',"Fine Fixtures",'Woodbrige']

for i in target_list:
    url = f'https://www.homedepot.com/s/{i}'

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_url = soup.find_all('a', {'class': "hd-pagination__link "})


    while len(next_url) != 0:
        with open("urls.txt", "a+", encoding="utf-8") as f:
            f.write(next_url[0].href + "\n")
        f.close()
        url_next = f'https://www.homedepot.com{next_url[0].href}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_url = soup.find_all('a', {'class': "hd-pagination__link "})
        no_product_elements = soup.select('.results-wrapped--no-products')
        if no_product_elements:
            break
        print(next_url)
        print(no_product_elements)
