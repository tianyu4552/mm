#!/usr/bin/python
# -*- coding:gbk -*-

# ��������exe��ʱ����Ҫת��Ϊinput(unicode('xxxx'��.encode('gbk'))
import sys
import website

reload(sys)
sys.setdefaultencoding('gbk')

# ��վ��ҳ
website_url = 'https://www.xxxx.com'
# Ʒ��-�����ֵ�
brand_name_href_dic = {}

if __name__ == '__main__':
    print u'ѡ�����ַΪ: xxx www.xxxx.com'
    channel_url = website.get_channel_url()
    print u'�����Ƶ��Ϊ: ' + channel_url
    brand_name_list = website.get_all_brand_name(channel_url)
    brand_key = website.choose_one_brand(brand_name_list)
    print u'ѡ���Ʒ����: ' + brand_name_href_dic[brand_key]
