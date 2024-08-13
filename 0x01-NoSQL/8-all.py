#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """Return a list of all documents in a collection"""
    col_lst = []
    for col in mongo_collection.find():
        col_lst.append(col)
    return col_lst
