import json
import re
import tweepy
from connection.mongodb.mongodbConnection import collection

from connection.twitter.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        post = collection.insert_one(json.dumps({
            "lang": status.lang,
            "coordinates": status.coordinates,
            "source": re.sub("\\\u003C.*?\\\u003E", '', status.source)
            #"hashtags": status.entities.get('hashtags')
            }, sort_keys=True)
            
        #post = collection.insert_one(status._json).inserted_id
        print(post)
        #if status.user.location != None:
            #print(status.user.location)
            # print(status.entities.get('hashtags'))

    # Twitter error list : https://dev.twitter.com/overview/api/response-codes

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

def start_stream():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)

    streamListener = TwitterStreamListener()

    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    while True:
        try:
            myStream.filter(locations=[-180,-90,180,90], async=True)
        except:
            pass

if __name__ == '__main__':
    start_stream()
