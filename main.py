#!/usr/bin/python
# -*- coding:gbk -*-

# ��������exe��ʱ����Ҫת��Ϊinput(unicode('xxxx'��.encode('gbk'))
import sys
import time
import uuid
import website

reload(sys)
sys.setdefaultencoding('gbk')

# ��վ��ҳ
website_url = 'https://www.vmei.com'
# Ʒ��-�����ֵ�
brand_name_href_dic = {}

if __name__ == '__main__':
    print u'ѡ�����ַΪ: Ψ����ױwww.vmei.com'
    channel_url = website.get_channel_url()
    print u'�����Ƶ��Ϊ: ' + channel_url
    brand_name_list = website.get_all_brand_name(channel_url)
    total_brand = ''
    for index in range(len(brand_name_list)):
        temp_info = '��' + str(index) + '��' + brand_name_list[index]
        total_brand += temp_info + '  '
        if (index != 0 and index % 5 == 0) or index == len(brand_name_list)-1:
            print total_brand
            total_brand = ''
