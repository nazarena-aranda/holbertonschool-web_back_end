#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    total = mongo_collection.count_documents({})
    print("{} logs".format(total))

    get_amount = mongo_collection.count_documents({"method": "GET"})
    post_amount = mongo_collection.count_documents({"method": "POST"})
    put_amount = mongo_collection.count_documents({"method": "PUT"})
    patch_amount = mongo_collection.count_documents({"method": "PATCH"})
    delete_amount = mongo_collection.count_documents({"method": "DELETE"})
    status_check_amount = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    print("Methods:")
    print("\t method GET: {}".format(get_amount))
    print("\t method POST: {}".format(post_amount))
    print("\t method PUT: {}".format(put_amount))
    print("\t method PATCH: {}".format(patch_amount))
    print("\t method DELETE: {}".format(delete_amount))
    print("{} status check".format(status_check_amount))