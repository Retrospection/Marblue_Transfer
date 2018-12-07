# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from flask import Flask, request, jsonify

from backend.model import Record
from backend.repository import Repository
from backend.utility import isValidRecord

app = Flask(__name__)
repository = Repository('./data/db.sqlite')

@app.route('/addRecord', methods=['POST'])
def addRecord():
    record = request.get_json()
    if isValidRecord(record) == 0:
        repository.addRecord(**record)
        return jsonify({
            'code': 200,
            'msg': '插入成功！'
        })
    else :
        return jsonify({
            'code': 400,
            'msg': '待插入记录有误！'
        })

@app.route('/query', methods=['POST'])
def query():
    queryOptions = request.get_json()
    result = repository.findByQQNumber(queryOptions['qq_number'])
    return jsonify({
        'code': 200,
        'msg': '查询成功',
        'data': result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3535, debug=True)