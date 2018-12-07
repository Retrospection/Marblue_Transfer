# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from datetime import date

from flask import Flask, request, jsonify
from flask_cors import CORS

from repository import Repository
from utility import isValidRecord

from error_code import (
    QQ_NUMBER_NOT_EXIST,
    FROM_GROUP_NOT_EXIST,
    TO_GROUP_NOT_EXIST
)

app = Flask(__name__)
repository = Repository('./data/db.sqlite')
CORS(app, supports_credentials=True)

@app.route('/addRecord', methods=['POST', 'OPTIONS'])
def addRecord():
    if request.method == 'OPTIONS':
        return 'ok'

    record = request.get_json()
    print(record)
    validatorResult = isValidRecord(record)

    if validatorResult == 0:
        repository.addRecord(qqNumber=record['qq_number'],
                             fromGroup=record['from_group'],
                             toGroup=record['to_group'])
        return jsonify({
            'code': 0,
            'msg': '插入成功！'
        })
    elif validatorResult == QQ_NUMBER_NOT_EXIST:
        return jsonify({
            'code': -1,
            'msg': 'qq号码有误'
        })
    elif validatorResult == FROM_GROUP_NOT_EXIST:
        return jsonify({
            'code': -1,
            'msg': '缺原群信息'
        })
    elif validatorResult == TO_GROUP_NOT_EXIST:
        return jsonify({
            'code': -1,
            'msg': '缺目标群信息'
        })


@app.route('/query', methods=['POST'])
def query():
    queryOptions = request.get_json()
    if ('qq_number' not in queryOptions and
        'start_date' not in queryOptions and
        'end_date' not in queryOptions):

        return jsonify({
            'code': 200,
            'msg': '查询成功',
            'data': repository.getAll()
        })
    if ('qq_number' in queryOptions and
        'start_date' not in queryOptions and
        'end_date' not in queryOptions):

        return jsonify({
            'code': 200,
            'msg': '查询成功',
            'data': repository.findByQQNumber(queryOptions['qq_number'])
        })

    if ('qq_number' not in queryOptions and
        'start_date' in queryOptions and
        'end_date' in queryOptions):
        return jsonify({
            'code': 200,
            'msg': '查询成功',
            'data': repository.findBetweenDate(queryOptions['start_date'] / 1000, queryOptions['end_date'] / 1000)
        })

    if ('qq_number' in queryOptions and
        'start_date' in queryOptions and
        'end_date' in queryOptions):
        return jsonify({
            'code': 200,
            'msg': '查询成功',
            'data': repository.findByQQNumberBetweenDate(queryOptions['qq_number'],
                                                         queryOptions['start_date'] / 1000,
                                                         queryOptions['end_date'] / 1000)
        })




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3535, debug=True)