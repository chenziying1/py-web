# -*- coding: utf-8 -*-
# time:2023/8/4 14:39
# file index.py
# outhor:czy
# email:1060324818@qq.com


with open("amzon_data.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
f.close()

while len(a) > 0:
    url = a[0].strip()
    if  "DeerValley" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_DeerValley_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif  "TOTO" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_TOTO_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "Swiss+Madison" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_Swiss_Madison_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "American+Standard" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_American_Standard_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "Kohler" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_Kohler_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "HOROW" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_HOROW_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "MOHOME" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_MOHOME_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "Fine+Fixtures" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_Fine_Fixtures_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "Woodbrige" in url:
        with open("../爬取网站下对应的品牌/amzon/amzon_Woodbrige_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    else:
        with open("amzon/amzon_other_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
