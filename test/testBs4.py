# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: testBs4.py
# @time: 2021/6/27 10:31
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.body)
# print(type(bs.head))
# print(bs.title.string)
# print(type(bs.title.string))
# print(bs.a.attrs)
# print(bs)
# print(bs.a.string)
# print(type(bs.a.string))


# ---------------------------

# print(bs.head.contents)
# 文档搜索
# 字符串过滤
# t_list = bs.find_all("a")
# print(t_list)
# 正则搜索使用search()匹配
# t_list = bs.find_all(re.compile("a"))
# 方法搜索根据函数搜素

# def name_is_exists(tag):
#     return tag.has_attr("name")
#
#
# t_list = bs.find_all(name_is_exists)


# print(t_list)

# 2kwargs参数
# t_list=bs.find_all(id="head")
# t_list = bs.find_all(class_="mnav")
# for item in t_list:
#     print(item)
# # print(t_list)


# text参数
# t_list=bs.find_all(text="新闻")
# t_list=bs.find_all(text=["新闻","贴吧"])
# t_list = bs.find_all(text=re.compile("\d"))  # 正则表达式


# 4.limit参数
# t_list = bs.find_all("a", limit=3)
# for item in t_list:
#     print(item)


# 选择器
# t_list = bs.select("title")
# t_list = bs.select(".mnav")
# t_list=bs.select("#u1")
t_list = bs.select("a[class='mnav c-font-normal c-color-t']")
# t_list = bs.select("head > title") #通过子标签查找
# t_list = bs.select(".manv ~ .bri")
# for item in t_list:
print(t_list[2].get_text())
