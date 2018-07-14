#!/usr/bin/python
# -*- coding:utf-8 -*-


import os
import os.path
import urllib
import globalvar as gl
import pid_random as pr
import xlwt


# -- img标签数组保存函数 ---
def store_scroll_img_list(brand_name, product_id, img_list):
    for img in img_list:
        img_url = img.get('src')
        img_name = pr.get_random_str(6) + '.jpg'
        store_product_img(brand_name, product_id, img_name, img_url)


def store_box_img_list(brand_name, product_id, img_list):
    for img in img_list:
        img_url = img.get('data-original')
        img_name = pr.get_random_str(6) + '.jpg'
        store_product_img(brand_name, product_id, img_name, img_url)


# -- 图片保存函数 ---
# brand_name 品牌名称
# product_id 货品id
# file_name 图片名称
# img_url 图片连接
def store_product_img(brand_name, product_id, file_name, img_url):
    brand_name = brand_name.replace('/', '_')
    file_name = file_name.replace('/', '_')
    file_path = gl.root_dir + '/' + brand_name + '/' + product_id
    make_dir(file_path)
    file_url = file_path + '/' + file_name
    img_url = img_url.replace('hhttp', 'http')
    urllib.urlretrieve(img_url, file_url)


# 判断路径是否存在, 如果不存在则创建
def make_dir(path):
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
    return


def export_to_excel(brand_name, product_name_id_dic):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('sheet1')

    wrapper_title(worksheet)

    body_font_style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'宋体'
    # 字体大小
    font.height = 0x00E0
    body_font_style.font = font

    for (key, value) in product_name_id_dic.items():
        line = worksheet.last_used_row + 1
        worksheet.write(line, 0, key, body_font_style)
        worksheet.col(0).width = 30000
        worksheet.write(line, 1, value, body_font_style)
        worksheet.col(1).width = 7000

    file_name = brand_name.replace('/', '') + '.xls'
    # 文件保存
    workbook.save(file_name)


def wrapper_title(worksheet):
    fontStyle = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'宋体'
    font.bold = True
    # 字体大小
    font.height = 0x0100
    fontStyle.font = font

    # 居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    fontStyle.alignment = alignment

    title_list = [u'商品名称', u'商品ID']

    for index, title in enumerate(title_list):
        worksheet.write(0, index, title, fontStyle)
        # 标题宽度
        worksheet.col(index).width = 30000


# if __name__ == '__main__':
#     file_object = get_file_object('AHC 艾米', '508377')
#     write_2_file(file_object, 'title:' + 'aaaaa')
#     write_2_file(file_object, 'body:' + 'bbbbbb')
#     file_object.close()
#     store_product_img('AHC 艾米', '508377', '1A69165B9E644347ADB187B5E1F39B88.jpg', 'https://img01.vmei.com/201604/1A69165B9E644347ADB187B5E1F39B88.jpg@350w_350h_90Q_1e_1c.src')

