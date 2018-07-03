#!/usr/bin/python
# -*- coding:utf-8 -*-

# 网站主页
website_url = 'https://www.vmei.com'

# 保存文件的路劲
root_dir = "."

# 品牌-链接字典
global brand_name_href_dic
brand_name_href_dic = {}


def set_value(key, value):
    brand_name_href_dic[key] = value


def get_value(name, defValue=None):
    try:
        return brand_name_href_dic[name]
    except KeyError:
        return defValue


def clear_value():
    brand_name_href_dic = {}
