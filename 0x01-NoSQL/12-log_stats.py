#!/usr/bin/env python3
"""A Python script that provides some stats
about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_dict = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    total_logs = 0
    status_check = 0

    for log in nginx_coll.find():
        total_logs += 1
        if log.get('method') in method_dict:
            method_dict[log.get('method')] += 1
        if log.get('method') == 'GET' and log.get('path') == '/status':
            status_check += 1

    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, method_dict.get(method)))
    print("{} status check".format(status_check))