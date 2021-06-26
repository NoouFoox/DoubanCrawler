# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: spider.py
# @time: 2021/6/26 19:18

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    print("开始爬取········")
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    # 保存数据
    savepath = ".\\豆瓣电影xls"
    # saveData(savepath)
    askUrl(baseurl)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)
    return datalist


# 得到一个指定url的网页信息
def askUrl(url):
    # 用户代理
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        repo = urllib.request.urlopen(request)
        html = repo.read().decode("utf-8")
        print(html)
        # 错误处理
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(savapath):
    print("1")


if __name__ == "__main__":
    main()
