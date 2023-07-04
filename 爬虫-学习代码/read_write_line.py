import os
f = open('urls.txt','r+')
url = ""
while True:
          url = f.readline()
          url = url.rstrip()
          if url == "":
                    break
          else:
                    print(url)
print()
f.seek(0)
print(f.readlines())
f.write('https://mikoto.iwara.tv/file.php?expire=1659482139&hash=5a0a9e534d01c7299551d304b4f80a4fee00e1a6&file=2022%2F05%2F24%2F1653381674_Y88k7febwkt5ea8b5_540.mp4&op=dl&r=0'+os.linesep)
f.close()
