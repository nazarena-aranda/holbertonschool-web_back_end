#!/usr/bin/env python3
"""
Change school topics
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """python function that changes all topics of a school document"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
