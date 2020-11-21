import pymongo
from bson.json_util import dumps
import json

mongo = pymongo.MongoClient('mongodb+srv://nivedita:Hello123!@cluster0.mjent.mongodb.net/mydatabase?retryWrites=true&w=majority', maxPoolSize=50, connect=False)

db = pymongo.database.Database(mongo, 'mydatabase')
col = pymongo.collection.Collection(db, 'mycollection')

col_results = json.loads(dumps(col.find().limit(5).sort("time", -1)))