import tweepy
import geopy

consumer_key = "4YZgGzc5bB4jMwoTJBDXKy8gp"
consumer_secret = "PiQosIV3Lnss42kf52UNvOkFY0e1k2YX4XX7oqp3Pb6LkKCHvE"

access_token = "231255197-C4sRvE2QDFxVgViH7h4G6C0nFz6sEdsRWk87V6sI"
access_token_secret = "1LUZ4lKfbsXGaLzF4I0c0ToIMJVEcp8zeZsmHaHWFlwba"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
geolocator = geopy.Nominatim()

for tweet in public_tweets:
    #if tweet.coordinates != None:
    print(tweet.user.location)
    print(geolocator.geocode(tweet.user.location))