#!/usr/bin/env python3
"""
Change school topics
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic
    """
    return mongo_collection.find({ "topics": topic })