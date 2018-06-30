#!/usr/bin/python
# -*- coding:gbk -*-

# 打包输出成exe的时候，需要转化为input(unicode('xxxx'）.encode('gbk'))
import sys
import time
import uuid
import website

reload(sys)
sys.setdefaultencoding('gbk')

# 网站主页
website_url = 'https://www.vmei.com'
# 品牌-链接字典
brand_name_href_dic = {}

if __name__ == '__main__':
    print u'选择的网址为: 唯美美妆www.vmei.com'
    channel_url = website.get_channel_url()
    print u'进入的频道为: ' + channel_url
    brand_name_list = website.get_all_brand_name(channel_url)
    total_brand = ''
    for index in range(len(brand_name_list)):
        temp_info = '【' + str(index) + '】' + brand_name_list[index]
        total_brand += temp_info + '  '
        if (index != 0 and index % 5 == 0) or index == len(brand_name_list)-1:
            print total_brand
            total_brand = ''
