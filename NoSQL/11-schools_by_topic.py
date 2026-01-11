#!/usr/bin/env python3
""" Module that returns schools having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school documents having a specific topic """
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))
