# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from flask import Flask, request, jsonify

from backend.repository import Repository
from backend.utility import isValidRecord

from backend.error_code import (
    QQ_NUMBER_NOT_EXIST,
    FROM_GROUP_NOT_EXIST,
    TO_GROUP_NOT_EXIST
)

app = Flask(__name__)
repository = Repository('./data/db.sqlite')

@app.route('/addRecord', methods=['POST'])
def addRecord():

    record = request.get_json()
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
    result = []
    if len(queryOptions) == 0:
        result = repository.getAll()
    if 'qq_number' in queryOptions:
        result = repository.findByQQNumber(queryOptions['qq_number'])
    if 'from_group' in queryOptions:
        result = list(set(result) and set(repository.findByFromGroup(queryOptions['from_group'])))
    if 'to_group' in queryOptions:
        result = list(set(result) and set(repository.findByToGroup(queryOptions['to_group'])))
    if 'start_date' in queryOptions and 'end_date' in queryOptions:
        result = list(set(result) and set(repository.findBetweenDate(queryOptions['start_date'],
                                                                     queryOptions['end_date'])))
    print(result)
    return jsonify({
        'code': 200,
        'msg': '查询成功',
        'data': result
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3535, debug=True)