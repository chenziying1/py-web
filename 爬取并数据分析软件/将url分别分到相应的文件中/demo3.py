# -*- coding: utf-8 -*-
# time:2023/8/4 14:39
# file index.py
# outhor:czy
# email:1060324818@qq.com


with open("wayfair_data.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
f.close()

while len(a) > 0:
    url = a[0].strip()
    if  "deervalley" in url:
        with open("wayfair/wayfair_DeerValley_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif  "toto" in url:
        with open("wayfair/wayfair_TOTO_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "swiss-madison" in url:
        with open("wayfair/wayfair_Swiss_Madison_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "american-standard" in url:
        with open("wayfair/wayfair_American_Standard_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "kohler" in url:
        with open("wayfair/wayfair_Kohler_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "horow" in url:
        with open("wayfair/wayfair_HOROW_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "mohome" in url:
        with open("wayfair/wayfair_MOHOME_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "fine-fixtures" in url:
        with open("wayfair/wayfair_Fine_Fixtures_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "woodbrige" in url:
        with open("wayfair/wayfair_Woodbrige_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    else:
        with open("wayfair/wayfair_other_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
