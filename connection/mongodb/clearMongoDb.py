from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.twitter
db.tweets.drop()

db.createCollection('tweets', capped=True, size = 200000000)
