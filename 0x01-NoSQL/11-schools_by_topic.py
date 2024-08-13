#!/usr/bin/env python3
"""FInds all document in a collection with a
specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return list of documents with a specific topic"""
    return [c for c in mongo_collection.find() if topic in c.get("topics")]
