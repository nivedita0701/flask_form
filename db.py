from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = 'mongodb+srv://nivedita:Hello123!@cluster0.mjent.mongodb.net/mydatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('mydatabase')
user_collection = pymongo.collection.Collection(db, 'mycollection')