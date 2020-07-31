import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('192.168.126.135', port=27017)

db = client.test
print(db)



