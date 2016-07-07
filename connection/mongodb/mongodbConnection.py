from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.twitter

collection = db.tweets

cursor = db.tweets.find()

print(cursor.count())