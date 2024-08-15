#!/usr/bin/env python3
"""Print logs from a nginx server"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.log.nginx

    logs_data = nginx_collection.find()
    print(logs_data)
