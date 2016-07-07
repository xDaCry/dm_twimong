import tweepy
from connection.mongodb.mongodbConnection import collection

from connection.twitter.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        post = collection.insert_one(status._json).inserted_id
        print(post)
        #if status.user.location != None:
            # print(status.user.location)
            # print(status.entities.get('hashtags'))
            #print(status.source)
            # geolocator = geocoders.GoogleV3
            # location = geolocator.geocode(status.user.location)
            # print(status.user.location,"=",(location.latitude, location.longitude))
            # print((location.latitude, location.longitude))
            # time.sleep(1)

    # Twitter error list : https://dev.twitter.com/overview/api/response-codes

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False


    #def on_error(self, status_code):
    #    print >> sys.stderr, 'Encountered error with status code:', status_code
    #    return True # Don't kill the stream
    #    print("Stream restarted")

def start_stream():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)

    streamListener = TwitterStreamListener()

    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    while True:
        try:
            myStream.sample(async=True)
        except:
            pass

if __name__ == '__main__':
    start_stream()