# 第2节：静态网页抓取

*Date in 21/11/2024 Made by Tianlang*

声明：仅供个人学习使用 参考资料来源于 **Python网络爬虫从入门到实践**

## 2.1安装Requests库

```powershell
pip install requests
```

Request库的功能是获取某个网页的内容<br/>

## 2.2获取相应内容

```python
import requests
r=requests.get('https://github.com/Tianlang-create')
print("文本编码: "+r.encoding)
print("状态码: "+str(r.status_code))
```

​		tips:库request的get函数获取了目标函数的网页数据*递给*r这样就获取了网页数据。但是有些网页需要对Requests的参数进行设置<br/>

## 2.3定制Requests参数

### 1>传递URL参数

​		以键值对的形式进行URL访问，将要查询的形式存储在params参数里

```python
import requests
key_dict={'key1':'value1'}#,'key2':'value2'}
r=requests.get('https://httpbin.org/get',params=key_dict)
print("URL已经正确编码:"+r.url)
print("状态码:"+str(r.status_code))
print("文本内容(响应体):"+r.text)
```

* <u>传递URL参数在HTTP请求中具有多种用途，主要包括传递查询条件、指定资源、实现分页和排序、以及传递额外信息等，这些参数有助于服务器根据客户端的具体需求返回相应的数据或执行特定的操作</u>

<br/>

### 2>定制请求头

```python
import requests
headers={
    'user_agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    'Host':'www.santostang.com'
}
r= requests.get('http://www.santostang.com/', headers=headers)#不要加https://
print("状态响应码:"+str(r.status_code))

```

* <u>定制请求头可以增强HTTP请求的功能性、安全性和灵活性，满足复杂业务需求，优化性能，并帮助遵守网站规定和调试问题。</u>

  

### 3>发送post请求

​		当需要向服务器提交数据（如表单数据、文件上传等）时，通常会使用POST请求（如在登录时）。这些数据通常包含在请求的body中，并且可以是各种格式，如JSON、XML、表单数据或文件等。

```python
import requests
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=key_dict)
print (r.text)
```



### 4>超时处理

​		使用Requests的timeout参数设定标准时间内限制应答

```python
import requests
link="http://www.santostang.com/"
r=requests.get(link,timeout=0.001)
```



## 2.4 实战：Requests爬取TOP250电影数据

``` python
import requests


def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i + 1), "页响应状态码:", r.status_code)
        print(r.text)

get_movies()
```

