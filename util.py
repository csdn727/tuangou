#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author  : Rex Zhang
# datetime: 2012-08-20 16:12:58
# filename: util.py

import re
import time


def time_convert():
    '''get today's timestamp '''
    _format = "%Y-%m-%d"
    timestr = time.strftime("%Y-%m-%d")
    secs = int(time.mktime(time.strptime(timestr, _format)))
    return (secs, timestr)


def spaces2nbsp(s):

    if not s:
        return ""

    if re.findall(r"\s+", s) or '\n' in s:
        try:
            s = s.replace('\n', ' ')
            return re.sub(r'\s+', '&nbsp;', s)
        except Exception as e:
            print "error in spaces2nbsp", str(e)
            return s
    else:
        return s

import codecs


def bad_utf8(s):
    """only for chars that formated like u'\xe9\xa5\xad\xe5\x90\xa6' """
    return codecs.escape_decode(repr(s)[2:-1])[0]


def multikeysort(items, columns):
    "http://stackoverflow.com/questions/1143671/python-sorting-list-of-dictionaries-by-multiple-keys"
    from operator import itemgetter
    comparers = [((itemgetter(col[1:].strip()), -1) if col.startswith(
        '-') else (itemgetter(col.strip()), 1)) for col in columns]

    def comparer(left, right):
        for fn, mult in comparers:
            result = cmp(fn(left), fn(right))
            if result:
                return mult * result
        else:
            return 0
    #unique sort.
    return sorted(items, cmp=comparer)

from os.path import dirname as dirname
from os.path import join as pathjoin


def getPath(sufix=""):
    '''get absolute path of the current dir'''
    path = dirname(__file__)
    try:
        index = path.index("..")
        if index != -1:
            path = path[:index]
    except:
        pass
    return pathjoin(path, sufix).replace('\\', '/')
