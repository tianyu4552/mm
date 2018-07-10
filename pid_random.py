#!/usr/bin/python
# -*- coding:utf-8 -*-

import random as rdm


def get_random_str(length):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(length):
        str += rdm.choice(chars)
    return str
