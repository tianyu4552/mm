#!/usr/bin/python
# -*- coding:utf-8 -*-


import os
import os.path
import urllib

rootdir = "."


# -- 图片保存函数 ---
# brand_name 品牌名称
# product_id 货品id
# file_name 图片名称
# img_url 图片连接
def store_product_img(brand_name, product_id, file_name, img_url):
    file_path = rootdir + '/' + brand_name + '/' + product_id
    make_dir(file_path)
    file_url = file_path + '/' + file_name
    urllib.urlretrieve(img_url, file_url)
    return


# 判断路径是否存在, 如果不存在则创建
def make_dir(path):
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
    return

# store_product_img('AHC 艾米', '508377', '1A69165B9E644347ADB187B5E1F39B88.jpg', 'https://img01.vmei.com/201604/1A69165B9E644347ADB187B5E1F39B88.jpg@350w_350h_90Q_1e_1c.src')