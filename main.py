#!/usr/bin/python
# -*- coding:gbk -*-

# ��������exe��ʱ����Ҫת��Ϊinput(unicode('xxxx'��.encode('gbk'))
import sys
import website
import globalvar as gl


reload(sys)
sys.setdefaultencoding('gbk')

# ��վ��ҳ
website_url = 'https://www.vmei.com/'
# Ʒ��-�����ֵ�
brand_name_href_dic = {}

if __name__ == '__main__':
    print u'ѡ�����ַΪ: xxx www.xxxx.com'
    channel_url = website.get_channel_url()
    print u'�����Ƶ��Ϊ: ' + channel_url
    brand_name_list = website.get_all_brand_name(channel_url)
    brand_key = website.choose_one_brand(brand_name_list)
    brand_name_and_url = gl.brand_name_href_dic[str(brand_key)]
    separator_index = brand_name_and_url.index('|')
    brand_name = brand_name_and_url[0: separator_index - 1]
    brand_url = brand_name_and_url[separator_index + 1: len(brand_name_and_url)]
    print u'ѡ���Ʒ����: ' + brand_name
    website.fetch_brand_all_product(brand_name, brand_url)


