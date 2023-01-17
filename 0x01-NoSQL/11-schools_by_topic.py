"""A module that lists all documents by topics"""


def schools_by_topic(mongo_collection, topic):
    """list documents by topic"""
    return mongo_collection.find({"topics": topic})
