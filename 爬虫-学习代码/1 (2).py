Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: C:/Users/HP/Desktop/爬取小说.py =====================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 18, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.read().decode('utf-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 30: invalid start byte
>>> 
===================== RESTART: C:/Users/HP/Desktop/爬取小说.py =====================

>>> 
===================== RESTART: C:/Users/HP/Desktop/爬取小说.py =====================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 18, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.read().decode("UTF-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 30: invalid start byte
>>> 
===================== RESTART: C:/Users/HP/Desktop/爬取小说.py =====================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 16, in getgale
    slist = re.findall('<td>.*</td>',html)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python39\lib\re.py", line 241, in findall
    return _compile(pattern, flags).findall(string)
TypeError: cannot use a string pattern on a bytes-like object
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
[]
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.content
AttributeError: 'HTTPResponse' object has no attribute 'content'
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<http.client.HTTPResponse object at 0x0000027D228A64F0>
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 21, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 17, in getgale
    slist = re.findall('<td>.*</td>',html)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python39\lib\re.py", line 241, in findall
    return _compile(pattern, flags).findall(string)
TypeError: expected string or bytes-like object
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.read().decode('utf-8').split("\n")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 30: invalid start byte
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 16, in getgale
    slist = re.findall('<td>.*</td>',html)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python39\lib\re.py", line 241, in findall
    return _compile(pattern, flags).findall(string)
TypeError: cannot use a string pattern on a bytes-like object
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 16, in getgale
    slist = re.findall('<td.*>.*</td>',html)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python39\lib\re.py", line 241, in findall
    return _compile(pattern, flags).findall(string)
TypeError: cannot use a string pattern on a bytes-like object
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 16, in getgale
    slist = re.findall('<td class="L">.*</td>',html)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python39\lib\re.py", line 241, in findall
    return _compile(pattern, flags).findall(string)
TypeError: cannot use a string pattern on a bytes-like object
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.read().decode('ascll')
LookupError: unknown encoding: ascll
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.read().decode('ASCII')
UnicodeDecodeError: 'ascii' codec can't decode byte 0xbe in position 30: ordinal not in range(128)
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 20, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 14, in getgale
    html = response.read().decode('UTF-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 30: invalid start byte
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
['<td class="L"><a href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td class="L">&nbsp;</td><td class="L">&nbsp;</td><td class="L">&nbsp;</td>']
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 22, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 16, in getgale
    slist = re.findall('<td class="L">.*</td>',html)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python39\lib\re.py", line 241, in findall
    return _compile(pattern, flags).findall(string)
TypeError: expected string or bytes-like object
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/爬取小说.py", line 22, in <module>
    getgale("http://www.eshu9.org/shu/12/12576/")
  File "C:/Users/HP/Desktop/爬取小说.py", line 16, in getgale
    slist = re.findall('<td class="L">.*</td>',html).split("\td")
AttributeError: 'list' object has no attribute 'split'
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<re.Match object; span=(17, 22), match='href='>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<re.Match object; span=(17, 134), match='href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td cla>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<re.Match object; span=(17, 134), match='href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td cla>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<re.Match object; span=(17, 134), match='href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td cla>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<re.Match object; span=(17, 122), match='href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td cla>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
<td class="L"><a href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td class="L">&nbsp;</td><td class="L">&nbsp;</td><td class="L">&nbsp;</td>
<class 'str'>
<re.Match object; span=(17, 134), match='href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td cla>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td class="L">&nbsp;</td><td class="L">&nbsp;</td><td class="L">&nbsp;</td>
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
href="1832303.html">绝色校草萌萝莉第1部分阅读</a></td><td class="L">&nbsp;</td><td class="L">&nbsp;</td><td class="L"
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
href="1832303.html
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
"1832303.html
>>> 
================================================ RESTART: C:/Users/HP/Desktop/爬取小说.py ================================================
1832303.html
>>> 