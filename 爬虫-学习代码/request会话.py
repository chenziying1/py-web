import requests
session = requests.Session()
session.get("http://httpbin.org/cookies/set/name/czy")
r = session.get("http://httpbin.org/cookies")
print(r.text)
