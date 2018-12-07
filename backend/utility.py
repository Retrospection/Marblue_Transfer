# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from backend.error_code import (
    QQ_NUMBER_NOT_EXIST,
    FROM_GROUP_NOT_EXIST,
    TO_GROUP_NOT_EXIST
)


def isValidRecord(record):
    if 'qq_number' not in record:
        return QQ_NUMBER_NOT_EXIST
    elif 'from_group' not in record:
        return FROM_GROUP_NOT_EXIST
    elif 'to_group' not in record:
        return TO_GROUP_NOT_EXIST
    return 0

