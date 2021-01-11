import requests
import json
from lxml import html


login_page =  requests.get('http://yourwebsite/login')
print(login_page.status_code)
headers = login_page.headers
content = html.fromstring(login_page.content)
input_fields = content.xpath('//input')

payload = {}
payload["authenticity_token"] =""
payload["username"]="username"
payload["password"] = "password"
for input in input_fields:
    attrib_name = input.attrib['name']
    if(attrib_name=="authenticity_token"):
        payload["authenticity_token"] = input.attrib['value'] 


meta_fields = content.xpath("//meta")
for meta in meta_fields:
    if('name' in meta.attrib and meta.attrib['name']=='csrf-token'):
        payload['csrf-token'] = meta.attrib['content']
        print(meta.attrib['content']) 
  #  print(meta.attrib['name'])

 
print("*****")
 
cookie = headers['Set-Cookie']
#headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
new_headers={}
new_headers['cache-control'] = 'max-age=0, private,must-revalidate'
new_headers['Connection']='Keep-Alive'
new_headers['Content-Type']='text/html; charset=utf-8'
new_headers['etag']= headers['Etag']
new_headers['Referrer-Policy'] = headers['Referrer-Policy']
new_headers['server'] = headers['Server']
new_headers['X-Content-Type-Options'] = headers['X-Content-Type-Options']
new_headers['x-download-options'] = headers['x-download-options']
new_headers['x-frame-options'] = headers['x-frame-options']
new_headers['x-permitted-cross-domain-policies'] = headers['x-permitted-cross-domain-policies']
new_headers['x-request-id'] = headers['x-request-id']
new_headers['x-runtime'] = headers['x-runtime']
new_headers['x-xss-protection'] = headers['x-xss-protection'] 
new_headers['Content-Length'] = str(len(json.dumps(payload)))
new_headers['Date'] = headers["date"] 
new_headers['Cookie'] =cookie
new_headers['X-CSRF-TOKEN']= payload['csrf-token'] 
 
login_request =  requests.post('http://avicenna.datasel.com.tr/login', data=json.dumps(payload), headers = new_headers)

print(login_request) 