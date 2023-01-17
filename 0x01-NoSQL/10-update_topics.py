#!/usr/bin/env python3
"""A module Update a document"""


def update_topics(mongo_collection, name, topics):
    """Update a document"""
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
