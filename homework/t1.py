# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: t1.py
# @time: 2021/6/29 7:59

itemlist = [
    {"name": "板烧鸡腿堡", "pice": 16},
    {"name": "巨无霸", "pice": 15},
    {"name": "麻辣鸡腿堡", "pice": 16},
    {"name": "芝士汉堡包", "pice": 19},
    {"name": "培根牛肉堡", "pice": 19}
]
print("{0:*>48}".format(""))
print("欢迎光临小包子的汉堡店!")
print("本店售卖宇宙无敌汉堡包!")
print("本店为爱心折扣店,如果你是爱心会员，优惠更大哦!")
print("尊敬的客户,每次只能品尝一种汉堡哦!")
for item in itemlist:
    print("{}.{:10}{}元".format(itemlist.index(item) + 1, item["name"], item["pice"]))
print("{0:*>48}".format(""))
print("{0:*>48}".format(""))
print("{}".format("做一枚有态度、有思想的汉堡店（我骄傲)!"))
print("{:>22}".format("祝您今日购物愉快!"))
print("{:>24}".format("欢迎您再次光临!"))
print("{0:*>48}".format(""))
