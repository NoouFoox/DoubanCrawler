# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: t3.py
# @time: 2021/6/29 9:08

if_vip = "n"

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
humberger_number = eval(input("请输入要购买的汉堡编号:"))
humberger_quantity = eval(input("请输入要购买的汉堡数量:"))
if humberger_number > len(itemlist)  or humberger_number < 1:
    print("wa!我们之售卖以上{}种汉堡哦!新口味尽请期待!".format(len(itemlist)))
else:
    if_vip = input("请输入y或n证明您的会员信息")
    if if_vip == "y":
        print("您为本店会员可以享受会员价")
    elif if_vip == "n":
        print("不好意思哦，您目前还不是我们的会员，\n无法享受会员价喽，永远爱你么么哒!")
    else:
        print("我还是个小包子，您的输入我看不懂，您拿着小票问问大包子吧!")
    humberger_price = itemlist[humberger_number - 1]["pice"]
    total_money = humberger_price * humberger_quantity
    vip_money = total_money * 0.7
    print("您购买的汉堡是{}号汉堡,共购买{}个,总计{}元".format(humberger_number, humberger_quantity, total_money))
    if if_vip == "y":
        print("您可以享 受会员价,折后总价:{}".format(round(vip_money, 3)))
print("{0:*>48}".format(""))
print("{}".format("做一枚有态度、有思想的汉堡店（我骄傲)!"))
print("{:>22}".format("祝您今日购物愉快!"))
print("{:>24}".format("欢迎您再次光临!"))
print("{0:*>48}".format(""))
