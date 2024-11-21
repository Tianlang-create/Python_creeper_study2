import requests
r=requests.get('https://github.com/Tianlang-create')
print("文本编码: "+r.encoding)
print("状态码: "+str(r.status_code))
#print("文本内容: "+r.text)

#写入到文本文件中
with open('github.html','w',encoding='utf-8') as f:
    f.write(r.text)

