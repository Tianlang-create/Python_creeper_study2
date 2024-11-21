import requests
key_dict={'key1':'value1'}#,'key2':'value2'}
r=requests.get('https://httpbin.org/get',params=key_dict)
print("URL已经正确编码:"+r.url)
print("状态码:"+str(r.status_code))
print("文本内容(响应体):"+r.text)

with open('Disign1','w',encoding='utf-8') as f:
    f.write(r.text)