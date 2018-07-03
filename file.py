#!/usr/bin/python
# -*- coding:utf-8 -*-


import os
import os.path
import urllib
import globalvar as gl


# -- 图片保存函数 ---
# brand_name 品牌名称
# product_id 货品id
# file_name 图片名称
# img_url 图片连接
def store_product_img(brand_name, product_id, file_name, img_url):
    brand_name.replace('/', '_')
    file_path = gl.root_dir + '/' + brand_name + '/' + product_id
    make_dir(file_path)
    file_url = file_path + '/' + file_name
    urllib.urlretrieve(img_url, file_url)


def get_file_object(brand_name, product_id):
    brand_name.replace('/', '_')
    file_path = gl.root_dir + '/' + brand_name + '/' + product_id
    make_dir(file_path)
    file_url = gl.root_dir + '/' + brand_name + '/' + product_id + '/' + 'context.txt'
    _file_object = open(file_url, 'w')
    return _file_object


def write_2_file(_file_object, context):
    _file_object.write(context + '\n')


# 判断路径是否存在, 如果不存在则创建
def make_dir(path):
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
    return

# if __name__ == '__main__':
#     file_object = get_file_object('AHC 艾米', '508377')
#     write_2_file(file_object, 'title:' + 'aaaaa')
#     write_2_file(file_object, 'body:' + 'bbbbbb')
#     file_object.close()
#     store_product_img('AHC 艾米', '508377', '1A69165B9E644347ADB187B5E1F39B88.jpg', 'https://img01.vmei.com/201604/1A69165B9E644347ADB187B5E1F39B88.jpg@350w_350h_90Q_1e_1c.src')

