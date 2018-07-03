#!/usr/bin/python
# -*- coding:utf-8 -*-

import random as rdm

def get_random_str():
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(18):
        str += rdm.choice(chars)
    return str

