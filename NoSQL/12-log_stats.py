#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    total = nginx_collection.count_documents({})
    print("{} logs".format(total))

    get_amount = nginx_collection.count_documents({"method": "GET"})
    post_amount = nginx_collection.count_documents({"method": "POST"})
    put_amount = nginx_collection.count_documents({"method": "PUT"})
    patch_amount = nginx_collection.count_documents({"method": "PATCH"})
    delete_amount = nginx_collection.count_documents({"method": "DELETE"})
    status_check_amount = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print("Methods:")
    print("\tmethod GET: {}".format(get_amount))
    print("\tmethod POST: {}".format(post_amount))
    print("\tmethod PUT: {}".format(put_amount))
    print("\tmethod PATCH: {}".format(patch_amount))
    print("\tmethod DELETE: {}".format(delete_amount))
    print("{} status check".format(status_check_amount))