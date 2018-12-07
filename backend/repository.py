# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import sqlite3
import datetime


class Repository(object):

    def __init__(self, dbFilename):
        self.dbFilename = dbFilename
        self.cursor = sqlite3.connect(self.dbFilename, check_same_thread=False)

    @staticmethod
    def __convertTimestampRecordToDatetime(record):
        return (record[0], record[1], record[2], record[3], datetime.datetime.fromtimestamp(record[4]).strftime('%Y-%m-%d %H:%M:%S'))

    def addRecord(self, qqNumber, fromGroup, toGroup):

        __ADD_RECORD_SQL = """
            INSERT INTO trans_records (qq_number, from_group, to_group, date)
            VALUES ({}, {}, {}, {});
        """.format(qqNumber, fromGroup, toGroup, int(datetime.datetime.now().timestamp()))


        self.cursor.execute(__ADD_RECORD_SQL)
        self.cursor.commit()

    def getAll(self):
        __GET_ALL_SQL = """
            SELECT * FROM trans_records
        """

        return list(map(Repository.__convertTimestampRecordToDatetime,
                        self.cursor.execute(__GET_ALL_SQL)))

    def findByQQNumber(self, qqNumber):

        __FIND_BY_QQ_NUMBER_SQL = """
            SELECT * FROM trans_records WHERE qq_number = '{}';
        """.format(qqNumber)
        return list(map(Repository.__convertTimestampRecordToDatetime,
                        self.cursor.execute(__FIND_BY_QQ_NUMBER_SQL).fetchall()))

    def findBetweenDate(self, startDate, endDate):

        __FIND_BETWEEN_DATE_SQL = """
            SELECT * FROM trans_records WHERE date > {} AND  date < {}
        """.format(startDate, endDate)

        return list(map(Repository.__convertTimestampRecordToDatetime,
                        self.cursor.execute(__FIND_BETWEEN_DATE_SQL).fetchall()))

    def findByQQNumberBetweenDate(self, qqNumber, startDate, endDate):
        __FIND_BY_QQNUMBER_BETWEEN_DATE_SQL = """
            SELECT * FROM trans_records WHERE qq_number = {} AND date > {} AND  date < {}
        """.format(qqNumber, startDate, endDate)

        return list(map(Repository.__convertTimestampRecordToDatetime,
                        self.cursor.execute(__FIND_BY_QQNUMBER_BETWEEN_DATE_SQL).fetchall()))

    def findByFromGroup(self, fromGroup):

        __FIND_BY_FROM_GROUP_SQL = """
            SELECT * FROM trans_records WHERE from_group = {}
        """.format(fromGroup)

        return list(map(Repository.__convertTimestampRecordToDatetime,
                        self.cursor.execute(__FIND_BY_FROM_GROUP_SQL).fetchall()))

    def findByToGroup(self, toGroup):

        __FIND_BY_TO_GROUP_SQL = """
            SELECT * FROM trans_records WHERE to_group = {}
        """.format(toGroup)

        return list(map(Repository.__convertTimestampRecordToDatetime,
                        self.cursor.execute(__FIND_BY_TO_GROUP_SQL).fetchall()))

if __name__ == '__main__':
    repository = Repository('./data/db.sqlite')
    repository.addRecord('371373446', 1, 2)
    print(repository.findByQQNumber('371373446'))