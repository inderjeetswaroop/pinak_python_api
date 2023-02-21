import pymongo

def connectDb():
    return pymongo.MongoClient("mongodb://localhost:27017")