# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: testRe.py
# @time: 2021/6/27 17:28
# 正则表达式

import re

# 创建模式对象
# pat = re.compile("AA")  # 此处AA为正则表达式
# m = pat.search("ABCAA")  # search 被校验的内容
# m = pat.search("AABCAADDDDCCCAAAA")

# 没有模式对象
# m = re.search("asd", "Aasd") # 前面是模板 后面是校验对象
# print(m)
# print(re.findall("a","ASDaDFAa"))
# print(re.findall("[A-Z]+","DsASDaDFAa"))

# sub替换

print(re.sub("a", "A", "abcdcasd"))  # 找到a用A替换

# 建议在在正则表达式中 被比较的字符串前面加r

a = r"\aabd-\'"
print(a)
