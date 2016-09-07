from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.twitter

result = db.tweets.aggregate([{"$group":{"_id":"$lang", "count":{"$sum":1}}},{"$sort": {"count": -1}},{"$limit": 5}])

print(list(result))