#!/usr/bin/python
# -*- coding:utf-8 -*-

# 网站主页
website_url = 'https://www.vmei.com'

# 保存文件的路劲
root_dir = "."

# 品牌-链接字典
global brand_name_href_dic
brand_name_href_dic = {}


# 商品名称-product_id字典
global product_name_id_dic
product_name_id_dic = {}


def set_value(dic, key, value):
    dic[key] = value


def get_value(dic, name, defValue=None):
    try:
        return dic[name]
    except KeyError:
        return defValue


def clear_value(dic):
    dic = {}
