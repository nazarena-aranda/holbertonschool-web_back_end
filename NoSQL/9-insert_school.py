#!/usr/bin/env python3
"""
insert a document in a collection
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Python function that inserts a new document in a collection based on kwargs """
    
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id