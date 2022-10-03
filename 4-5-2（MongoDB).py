import pymongo

MONGO_CONNETTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNETTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


def save_data(data):
    collection.update_one({name: data.get('name')},
                          {'$set': data},
                          upsert=True)
