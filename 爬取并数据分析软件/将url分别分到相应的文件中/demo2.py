# -*- coding: utf-8 -*-
# time:2023/8/4 14:39
# file index.py
# outhor:czy
# email:1060324818@qq.com


with open("homedeport_data.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
f.close()

while len(a) > 0:
    url = a[0].strip()
    if  "DEERVALLEY" in url:
        with open("homedeport/homedeport_DeerValley_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif  "TOTO" in url:
        with open("homedeport/homedeport_TOTO_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "Swiss-Madison" in url:
        with open("homedeport/homedeport_Swiss_Madison_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "American-Standard" in url:
        with open("homedeport/homedeport_American_Standard_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "KOHLER" in url:
        with open("homedeport/homedeport_Kohler_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "HOROW" in url:
        with open("homedeport/homedeport_HOROW_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "MOHOME" in url:
        with open("homedeport_MOHOME_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "FINE-FIXTURES" in url:
        with open("homedeport/homedeport_Fine_Fixtures_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    elif "WOODBRIDGE" in url:
        with open("homedeport/homedeport_Woodbrige_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
    else:
        with open("homedeport/homedeport_other_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
            print(str(url))
        f.close()
        a.pop(0)
