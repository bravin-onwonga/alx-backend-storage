#!/usr/bin/env python3
"""Insert document into collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts list of kwargs into a collection
    Params:
        mongo_collection: pymongo collection object
        kwargs: list of arguments to add
    """
    col = mongo_collection.insert_one(kwargs)
    return col.inserted_id
