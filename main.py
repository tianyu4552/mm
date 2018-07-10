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
    print u'欢迎进入: xxx www.xxxx.com'
    is_change_channel = True
    channel_url = ''
    while True:
        if is_change_channel:
            channel_url = website.get_channel_url()
            print u'进入的频道为: ' + channel_url
            is_change_channel = False
        brand_name_list = website.get_all_brand_name(channel_url)
        brand_key = website.choose_one_brand(brand_name_list)
        brand_name_and_url = gl.brand_name_href_dic[str(brand_key)]
        separator_index = brand_name_and_url.index('|')
        brand_name = brand_name_and_url[0: separator_index]
        brand_url = brand_name_and_url[separator_index + 1: len(brand_name_and_url)]
        print u'选择的品牌是: ' + brand_name
        website.fetch_brand_all_product(brand_name, brand_url)
        print brand_name + u' 数据下载完毕!! '
        change_channel = ''
        try:
            change_channel = input('是否想要切换到其他栏目：[0]是，[回车，其他]否\r\n')
        except:
            is_change_channel = False
        if change_channel == str(0) or change_channel == 0:
            is_change_channel = True


