# -*- coding: utf-8 -*-
# time:2023/7/27 13:57
# file homedepot.py
# outhor:czy
# email:1060324818@qq.com

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie': 'THD_PERSIST=; THD_CACHE_NAV_PERSIST=; thda.u=243865ae-1789-3550-fcf1-3ae3f47423b6; DELIVERY_ZIP_TYPE=DEFAULT; _pxvid=e307a15e-29f5-11ee-9937-b5137eb47646; _px_f394gi7Fvmc43dfg_user_id=ZTUwN2JkMDAtMjlmNS0xMWVlLTgwM2QtNWRmOGNkNzI0Njlk; QuantumMetricUserID=d5aee330d159889c5737ce0a9f0b1728; ajs_anonymous_id=4b6779ca-5559-419c-ba81-9d64328e83ab; _meta_facebookPixel_beaconFired=1690184672764; _meta_bing_beaconFired=1690184672766; _meta_neustar_mcvisid=19502600107476188242762195511795620360; _meta_movableInk_mi_u=4b6779ca-5559-419c-ba81-9d64328e83ab; _meta_metarouter_timezone_offset=-480; _meta_inMarket_userNdat=C470212DE32BBE64240C7669028A8E16; _meta_amobee_uid=7224529370597234571; _meta_revjet_revjet_vid=5252015208722558780; trx=5252015208722558780; _meta_neustar_fabrickId=E1:f1hVO6EaPo8ojMW0M6qBsgxYtujE2JRRcclNKr_Ge-UKIdYuXE2SXsd8CJSgQsJeBxgyp7JyddNhKWD__EJaXk0gJeyPTaoL5MlG447TPWo; _meta_neustar_tuid=232493304515009662908; _meta_tapAd_id=ae1638ae-755c-4035-b2f9-b8657b8e03dc; HD_DC=origin; akacd_usbeta=3867872664~rv=49~id=cd512ae0b623cbd805aae10fe77d6592; THD_NR=1; at_check=true; THD_SESSION=; THD_CACHE_NAV_SESSION=; DELIVERY_ZIP=90255; thda.s=6c638b57-540d-4731-0cc4-46ddc54fd5f5; AMCVS_F6421253512D2C100A490D45%40AdobeOrg=1; _meta_acuityAds_auid_failure=failed to make request; _meta_acuityAds_cauid_failure=failed to make request; thda.m=19502600107476188242762195511795620360; _meta_yahooMedia_yahoo_id_failure=timeout; _meta_pinterest_derived_epik_failure=timeout; _meta_pinterest_pin-unauth_failure=timeout; aam_uuid=19793098313355285732752287359615775869; _meta_mediaMath_mm_id=e18d645e-1bae-4b00-8b42-c3ae4d3cf61d; _meta_mediaMath_cid=e18d645e-1bae-4b00-8b42-c3ae4d3cf61d; LPVID=M0ZTZiZjJjYzEzZDdlZmY1; AKA_A2=A; bm_sz=4FE7878B3B280B2EE20A88537618FA59~YAAQRY0duMxT13iJAQAAzYPplRQ2/X9lFcLyLUR5tfJDBZnxbZBI6gwB0FLYke7PKQEVevYcET+ThKpX0rmucJqq3pOLRFyiM6O7EuZYlg3xdmtc8zutvCiyMHQ+HVmrxtk4qVa/IyMcPQ64iw+41SJTEQyRB9enZCFib/2q3A9StBHayHi8koI1nHdny6RFmJKplEKyYI1PFwIm9V9tPkJOVZmYsrpYPFhfhOTcK9t74/klam/ynVwKLeHenOtxHY4kq/uGShTl6Eg7OLlq5R/QEvAN8rVoUysIWZEqR1EA9EfF4NE=~3551297~4469817; x-ttsearch=ca_elasticpecos; ak_bmsc=F957B4E1D0868C3ED602EF0352347F2B~000000000000000000000000000000~YAAQRY0duHBU13iJAQAAqpXplRTv2TRR+c5rfwi5UVi5aql5Kb9NySAI9KGhQs30eUovC4fsz/zP7vTeWlA4z0o/4hKWhKuoENysRJUZ2JlP95twnNmVrOj0ndlc7LxZ+vFbvN2m8UWI3CY5vwZcmZdmIA2EbuBpGRAJdAqhkKBHcXOjQsYhy7eTBGVjgFYh9KQm1A63wMerIbpqtGO/L6Oxviczz0NQUmzK6EqQVrgq+bZuGQ4ur0nY5Ggw9OjyXlCwmj58Ik16fDxTrRzk9DbEYQW7ZYXP3CDdp4uU9FTdeRVqCRtCG6Pl64XWMHZJKrwuJ6Gz6ijrdimgg+2J/ewXeVKkrlvnY61LqWvKS63s/aOwz7BliWL3HbZjxGfhetgBRE80r34Wva4WPCrHq0lSS8HHpxNdcZ8uk5H8toP2TG0JabLsMJhTkEbOKi3naFH+A1c/9nrwB/GcXzPqdqUsSDkNoqi+XUs0X4U8kTNmsqbYCm583ooMZBuH3uM=; THD_LOCALIZER=%7B%22WORKFLOW%22%3A%22LOC_HISTORY_BY_IP%22%2C%22THD_FORCE_LOC%22%3A%221%22%2C%22THD_INTERNAL%22%3A%220%22%2C%22THD_LOCSTORE%22%3A%221002%2BHuntington%20Park%20-%20Huntington%20Park%2C%20CA%2B%22%2C%22THD_STRFINDERZIP%22%3A%2290255%22%2C%22THD_STORE_HOURS%22%3A%221%3B7%3A00-20%3A00%3B2%3B6%3A00-22%3A00%3B3%3B6%3A00-22%3A00%3B4%3B6%3A00-22%3A00%3B5%3B6%3A00-22%3A00%3B6%3B6%3A00-22%3A00%3B7%3B6%3A00-22%3A00%22%2C%22THD_STORE_HOURS_EXPIRY%22%3A1690440871%7D; ecrSessionId=F3EAC5513BD9D93F1366CA02BAD556E5; AMCV_F6421253512D2C100A490D45%40AdobeOrg=1585540135%7CMCMID%7C19502600107476188242762195511795620360%7CMCAAMLH-1691042088%7C9%7CMCAAMB-1691042088%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1690444488s%7CNONE%7CMCCIDH%7C240044181%7CvVersion%7C4.4.0; _meta_adobe_aam_uuid=19793098313355285732752287359615775869; _meta_googleGtag_ga=GA1.2.2096017905.1690437288; _meta_googleGtag_ga_library_loaded=1690437288667; _meta_adobe_neustar=1690437288678; _meta_adobe_google=1690437288679; _meta_adobe_microsoft=1690437288680; _meta_neustar_aam=19793098313355285732752287359615775869; _meta_metarouter_sessionID=1690437288663; _meta_adobe_fire={"xandr":false,"revjet":true,"mediaMath":true}; QuantumMetricSessionID=f787693e24d178afeb47ad48c8a0a5e0; _gcl_au=1.1.442251437.1690437295; _ga=GA1.2.2096017905.1690437288; _gid=GA1.2.1289117859.1690437296; LPSID-31564604=0z0-bb-4RaSeHvRSM77Hig; _ga_9H2R4ZXG4J=GS1.1.1690437295.1.1.1690437988.60.0.0; _meta_mediaMath_iframe_counter=5; s_sq=%5B%5BB%5D%5D; akavpau_prod=1690439654~id=21db4d7f7d92cf480b5f79c319fb6a46; mbox=session#19688b705bae49689f0c1076193996fa#1690441220|PC#19688b705bae49689f0c1076193996fa.35_0#1753684160; IN_STORE_API_SESSION=TRUE; _px=8EVx7hMg3Za5CaQ5ASAR7ls8BxGGSnC+5ff+TK9JX+Fi7K048VsHfzbpD7zjyxlHX4fef0ALEGU7oi9g/cr70Q==:1000:mfGJLrBdkxxMlxaOUY5+aKg6mZOJp4NzondQF+XmqCiH4ym77D4wZnijcqz6HPvTGXPLn1UAWKFqluShsjMi8xF/Fr+thwAJPWeXVgRC2RvP977kBrVyLmC/O/SGS0Zk1GGqP3jV31LRhgIrKWoZXt++V89byA3aI3u0pRU/R1rumxRjDnnrr4DqwwrDDjmYBDnFJno9zAzTKRQjdOn2bDlk6INIQu7m0u/fuChxNcnqrIx+TuDc1gznoycP6rIhnaLvozZFqXIyeK1OTjFVMA==; _abck=5A3B2AAAE8E715FBF77EEC2CC700DACD~0~YAAQhc9YaFhDbpWJAQAA5MIJlgout30aiiHZCseqQ2WbkQD4jjSLLYpuoAq06zH5QfjikMUVKJGN8aSrvRPwkdf5a7F3D+0vTJrG4+y7uO5tIRk4LSkHPmZ09mytmUGad80TCSf1yKbHRmBhCwU2FjsJSnexQMBDafGzoHos7zzVjvoyKqJ7wUvbMKmd+6zjaHnYHLTm64ec3sLp9vpbDTbhqQKu5Yjl+Bnl8wlPqs5WTzRfniM7TMywWiV8IIZfpEeIg/vb+NsN3pjSF8h0A9nW2/MQBwG3cxHiWOatC8QsUbfAZ6oTTCErBq+NnqidCi3vSrwyKE1CbH4/ONpcYgGdACbHZxYbWUrIonay7g96eByBfRy2oHttk4SzcKfyF08e8sKnyBpzfWqntUp2rOLckWT8Qm5dZKp+~-1~-1~-1; _pxde=4d7f98aa37d9a2dc4f21039b7e6057a51cc8ba56d373422045c05cb2471acd15:eyJ0aW1lc3RhbXAiOjE2OTA0MzkzNjk1NzYsImluY19pZCI6WyIyZTRkZjc2OTk2Njg0MzRhNDIwN2ZiYTJjNjZhNmQxYiJdfQ==; forterToken=e8c67bae9c60499f88e0a882a24c4538_1690439384934__UDF43_13ck; QSI_HistorySession=https%3A%2F%2Fwww.homedepot.com%2Fs%2FDeerValley%3FNao%3D48~1690438624502%7Chttps%3A%2F%2Fwww.homedepot.com%2Fs%2FDeerValley%3FNao%3D24~1690438653849%7Chttps%3A%2F%2Fwww.homedepot.com%2Fs%2FDeerValley%3FNao%3D68~1690438891517%7Chttps%3A%2F%2Fwww.homedepot.com%2Fs%2FDeerValley%3FNao%3D24~1690439395214; s_pers=%20productnum%3D5%7C1693031396569%3B%20s_nr365%3D1690439398929-Repeat%7C1721975398929%3B%20s_dslv%3D1690439398933%7C1785047398933%3B; s_sess=%20s_pv_pName%3Dsearch%2520results%3B%20s_pv_pType%3Dsearch%2520results%3B%20s_pv_cmpgn%3D%3B%20s_pv_pVer%3Dplp%253Aversion%253Agen2%3B%20s_cc%3Dtrue%3B%20stsh%3D%3B; RT="z=1&dm=www.homedepot.com&si=0ab56f1f-809f-4226-9ffc-b10e3a468bf4&ss=lkkqp3ng&sl=7&tt=9nh&obo=6&rl=1&ld=1cdb0&r=1f9w3v2b&ul=1cdb1"'
}

target_list = ["DeerValley", "TOTO", 'Swiss Madison', 'American Standard', 'Kohler', 'HOROW', 'MOHOME', "Fine Fixtures",
               'Woodbrige']

for i in target_list:
    url = f'https://www.homedepot.com/s/{i}'

    for j in range(0, 5000, 24):
        url2 = f"https://www.homedepot.com/s/{i}?Nao={j}"

        response = requests.get(url2, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 判断是否为无信息页面
        no_product_elements = soup.select('.results-wrapped--no-products')
        no_product_elements2 = soup.find_all('div', {'class': "sui-text-lg sui-py-5 sui-font-light"})

        print(no_product_elements, no_product_elements2)
        if len(no_product_elements) > 0 or len(no_product_elements2) > 0:
            break
        else:
            with open("urls.txt", "a+", encoding="utf-8") as f:
                f.write(url2 + "\n")
            f.close()
            print(url2)





