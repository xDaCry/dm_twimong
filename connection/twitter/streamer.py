from tweepy import Stream, OAuthHandler, API
from tweepy.streaming import StreamListener
#from geopy import geocoders
import sys
#import time
#from http.client import IncompleteRead

from connection.twitter.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

class BasicListener(StreamListener):
    """ A listener handles tweets are the received from the stream. """
    def on_connect(self):
        """Called when the connection is made"""
        print("Connection to stream accomplished.")

    def on_status(self, status):
        if status.user.location != None:
            #print(status.user.location)
            #print(status.entities.get('hashtags'))
            print(status.source)
            #geolocator = geocoders.GoogleV3
            #location = geolocator.geocode(status.user.location)
            #print(status.user.location,"=",(location.latitude, location.longitude))
            #print((location.latitude, location.longitude))
            #time.sleep(1)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream
        print("Stream restarted")

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True  # Don't kill the stream
        print("Stream restarted")

if __name__ == '__main__':
    # authentication
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # listener instance
    listen = BasicListener()
    # settings for API
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
              retry_errors=5)
    # open connection
    stream = Stream(auth=api.auth, listener=listen, gzip=True, timeout=None)
    stream.sample()

def start_stream():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # listener instance
    listen = BasicListener()
    # settings for API
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)
    # open connection
    stream = Stream(auth=api.auth, listener = listen, gzip=True, timeout=None)
    stream.sample()