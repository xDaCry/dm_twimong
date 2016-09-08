
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.twitter
db.tweets.drop()

db = client.twitter
db.create_collection('tweets', capped=True, size = 200000000)