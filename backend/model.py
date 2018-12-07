# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from collections import namedtuple


class Record(namedtuple('Record', ['id', 'qqNumber', 'fromGroup', 'toGroup', 'date'])):
    pass

