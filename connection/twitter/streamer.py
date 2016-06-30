from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
#from geopy import geocoders
import sys
#import time
#from http.client import IncompleteRead

CONSUMER_KEY = "f8rxzhS2b7WL24Mg0kkhaY0MY"
CONSUMER_SECRET = "XdIJjqNkx4cc9b0tIFk7RYnEN7zAqZIJbewagPlfCij6dPfc7G"

ACCESS_KEY = "231255197-bGPXUvjSkRR6HxLIsdxWstVQdNNtfMCZm4Z7EeeH"
ACCESS_SECRET = "LH0bWWAFxPQdICGw883loEO1eVMIhSUz0w6ViVRF8wFDM"

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
    #print("Create Listencer Instance")
    listen = BasicListener()
    # open connection
    #print("Open connection")
    stream = Stream(auth, listen, gzip=True, timeout=None)
    stream.sample()


