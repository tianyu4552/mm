#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import globalvar as gl
import file


# 得到soup，因后文通用，直接放这儿就行了
def urlBS(url):
    if url is None or url == '':
        print u'访问的url是空的'
        return
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
        channel_key = input('请按序号输入你想要进入的频道，'
                            '【1】护肤，【2】彩妆，【3】香水，【4】身体护理\r\n')
    except:
        channel_key = 1
    return gl.website_url + channel_url[channel_key-1]


def get_all_brand_name(channel_url):
    soup = urlBS(channel_url)
    brand_li_list = soup.select('.filter_list .filter_attrs')[0].find_all('li')
    brand_name_list = []
    # 重置
    gl.clear_value(gl.brand_name_href_dic)
    gl.clear_value(gl.product_name_id_dic)

    for index in range(len(brand_li_list)):
        # 下标0是'全部'的链接
        if index > 0:
            brand_name = brand_li_list[index].a.get_text()
            brand_name_list.append(brand_name)
            brand_url = gl.website_url + brand_li_list[index].a.get('href')

            gl.set_value(gl.brand_name_href_dic, str(index - 1), (brand_name + '|' + brand_url))

    return brand_name_list


def choose_one_brand(brand_name_list):
    # 一行输出5个品牌
    one_line_brand = ''
    for index in range(len(brand_name_list)):
        temp_info = '[' + str(index) + ']' + brand_name_list[index]
        one_line_brand += temp_info + '  '
        if (index != 0 and index % 7 == 0) or index == len(brand_name_list) - 1:
            print one_line_brand
            one_line_brand = ''
    try:
        brand_key = input('请输入一个品牌左侧的序号\r\n')
    except:
        brand_key = input('输入异常，请重新输入一个品牌左侧的序号\r\n')
    return brand_key


# 抓取某个品牌下所有商品信息
def fetch_brand_all_product(brand_name, brand_url):
    soup = urlBS(brand_url)
    # 列表
    product_list = soup.select('.product_list .pro_item')
    for product in product_list:
        product_detail_url = product.a.get('href')
        html_index = product_detail_url.index('.html')
        # 9是/product/的长度
        product_id = product_detail_url[9: html_index]

        product_name = product.select('.props')[0].a.text
        gl.set_value(gl.product_name_id_dic, product_name, product_id)

        # 详情
        product_detail = urlBS(gl.website_url + product_detail_url)
        # 详情-轮播图
        scroll_img_list = product_detail.select('.spec-scroll .items img')
        file.store_scroll_img_list(brand_name, product_id, scroll_img_list)

        # 详情-商品信息图
        detail_box_imgs = product_detail.select('.pro_box_main')[0].find_all('img')
        file.store_box_img_list(brand_name, product_id, detail_box_imgs)

    file.export_to_excel(brand_name, gl.product_name_id_dic)



