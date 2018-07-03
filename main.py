#!/usr/bin/python
# -*- coding:gbk -*-

# 打包输出成exe的时候，需要转化为input(unicode('xxxx'）.encode('gbk'))
import sys
import website
import globalvar as gl


reload(sys)
sys.setdefaultencoding('gbk')

# 网站主页
website_url = 'https://www.vmei.com/'
# 品牌-链接字典
brand_name_href_dic = {}

if __name__ == '__main__':
    print u'选择的网址为: xxx www.xxxx.com'
    channel_url = website.get_channel_url()
    print u'进入的频道为: ' + channel_url
    brand_name_list = website.get_all_brand_name(channel_url)
    brand_key = website.choose_one_brand(brand_name_list)
    brand_name_and_url = gl.brand_name_href_dic[str(brand_key)]
    separator_index = brand_name_and_url.index('|')
    brand_name = brand_name_and_url[0: separator_index - 1]
    brand_url = brand_name_and_url[separator_index + 1: len(brand_name_and_url)]
    print u'选择的品牌是: ' + brand_name
    website.fetch_brand_all_product(brand_name, brand_url)


