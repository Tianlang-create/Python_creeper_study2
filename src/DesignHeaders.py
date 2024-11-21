import requests
headers={
    'user_agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    'Host':'www.santostang.com'
}
r= requests.get('http://www.santostang.com/', headers=headers)#不要加https://
print("状态响应码:"+str(r.status_code))
