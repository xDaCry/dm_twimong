from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.twitter
#db.tweets.drop()
collection = db.tweets

cursor = db.tweets.find()

print(cursor.count())