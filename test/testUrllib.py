# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: testUrllib.py
# @time: 2021/6/26 20:10
import urllib.request
import urllib.parse

# post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# re = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(re.read().decode("utf-8"))

# get请求
# try:
#     re = urllib.request.urlopen("http://httpbin.org/get")
#     print(re.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out! 请求超时!")

# re = urllib.request.urlopen("http://www.baidu.com")
# print("status 状态码:", re.status)
# print(re.getheader("Server"))
data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding="utf-8")
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
req = urllib.request.Request(
    url=url,
    headers=headers,
    method="POST",
)
resp = urllib.request.urlopen(req)
print(resp.read().decode("utf-8"))
