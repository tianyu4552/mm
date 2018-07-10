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


def get_file_object(brand_name, product_id):
    brand_name = brand_name.replace('/', '_')
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


def export_to_excel(brand_name):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('sheet1')

    wrapper_title(worksheet)

    for page_url in get_result_list:
        page_url = page_url.encode('utf-8').decode('utf-8')

        house_detail_url_list = gdfc.get_house_detail_url(page_url)

        for each in house_detail_url_list:
            line = worksheet.last_used_row + 1
            gdfc.write_to_excel(each, worksheet, line)


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

    title_list = [u'标题', u'电话', u'租金', u'房屋面积', u'户型', u'朝向', u'楼层',
                  u'类型', u'装修', u'房龄', u'小区', u'地址', u'房源描述']

    for index, title in enumerate(title_list):
        worksheet.write(0, index, title, fontStyle)
        # 标题宽度
        worksheet.col(index).width = 4500
# if __name__ == '__main__':
#     file_object = get_file_object('AHC 艾米', '508377')
#     write_2_file(file_object, 'title:' + 'aaaaa')
#     write_2_file(file_object, 'body:' + 'bbbbbb')
#     file_object.close()
#     store_product_img('AHC 艾米', '508377', '1A69165B9E644347ADB187B5E1F39B88.jpg', 'https://img01.vmei.com/201604/1A69165B9E644347ADB187B5E1F39B88.jpg@350w_350h_90Q_1e_1c.src')

