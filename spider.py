# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: spider.py
# @time: 2021/6/26 19:18

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
# import sqlite3


def main():
    print("开始爬取········")
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    # 保存数据
    savepath = "豆瓣电影Top250.xls"
    saveData(datalist, savepath)


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
finBD = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查护符合要求的字符串
            # print(item)
            data = []  # 保存一部电影的所有信息
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("\xa0/\xa0", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judegeNum = re.findall(findJudge, item)[0]
            data.append(judegeNum)
            Inq = re.findall(findInq, item)
            if len(Inq) != 0:
                data.append(Inq[0].replace("。", ""))
            else:
                data.append(" ")
            BD = re.findall(finBD, item)[0]
            BD = re.sub('<br(\s+)?/>(\s+)?', " ", BD)
            BD = re.sub('\xa0', "", BD)
            BD = re.sub('/', "", BD)
            data.append(BD.strip())  # 去掉空格
            datalist.append(data)
    # print(datalist)
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
        # print(html)
        # 错误处理
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, savapath):
    print("save...")
    # print(datalist)
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top5', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        # print(i + 1)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savapath)


if __name__ == "__main__":
    main()
    print("爬取完毕")
