from requests import Request,Session
url = "http://httpbin.org/post"
data = {
          'name':'Bill'
          }
session = Session()
req = Request('post',url,data=data)
prepared = session.prepare_request(req)
r = session.send(prepared)
print(r.text)
