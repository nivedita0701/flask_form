from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = 'mongodb+srv://hritik1234:hritik1234@hscluster.s6zw9.mongodb.net/HScluster?retryWrites=true&w=majority'

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('mydatabase')
user_collection = pymongo.collection.Collection(db, 'mycollection')