#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import main


# 得到soup，因后文通用，直接放这儿就行了
def urlBS(url):
    response = requests.get(url)
    if response.status_code == 404:
        print u'页面' + url + u'未找到'
    if response.status_code == 500:
        print u'服务器页面' + url + u'内部报错'
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# 通过交互的方式让搜索人输入条件，不输的话有默认值
def get_channel_url():
    # 频道
    channel_url = ['/nca-12-1.html', '/nca-13-1.html', '/nca-14-1.html', '/nca-15-1.html']
    try:
        channel_key = input(unicode('请按序号输入你想要进入的频道，【1】护肤，【2】彩妆，【3】香水，【4】身体护理'))
    except:
        channel_key = 1
    return main.website_url + channel_url[channel_key]


def get_all_brand_name(channel_url):
    soup = urlBS(channel_url)
    brand_ul_list = soup.select('.filter_list .filter_attrs')[0]
    brand_li_list = brand_ul_list.find_all('li')
    brand_name_list = []
    # 重置
    main.brand_name_href_dic = {}
    for index in range(len(brand_li_list)):
        if index > 0:
            brand_name = brand_li_list[index].a.get_text()
            brand_name_list.append(brand_name)
            brand_url = main.website_url + brand_li_list[index].a.get('href')
            main.brand_name_href_dic[brand_name] = brand_url

    return brand_name_list


def choose_one_brand(brand_name_list):
    # 一行输出5个品牌
    one_line_brand = ''
    for index in range(len(brand_name_list)):
        temp_info = '【' + str(index) + '】' + brand_name_list[index]
        one_line_brand += temp_info + '  '
        if (index != 0 and index % 5 == 0) or index == len(brand_name_list) - 1:
            print one_line_brand
            one_line_brand = ''
    try:
        brand_key = input(unicode('请输入一个品牌左侧的序号'))
    except:
        brand_key = input(unicode('输入异常，请重新输入一个品牌左侧的序号'))
    return brand_key
