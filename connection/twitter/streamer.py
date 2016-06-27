from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
from geopy.geocoders import Nominatim, Photon

from http.client import IncompleteRead

CONSUMER_KEY = "4YZgGzc5bB4jMwoTJBDXKy8gp"
CONSUMER_SECRET = "PiQosIV3Lnss42kf52UNvOkFY0e1k2YX4XX7oqp3Pb6LkKCHvE"

ACCESS_KEY = "231255197-C4sRvE2QDFxVgViH7h4G6C0nFz6sEdsRWk87V6sI"
ACCESS_SECRET = "1LUZ4lKfbsXGaLzF4I0c0ToIMJVEcp8zeZsmHaHWFlwba"

class BasicListener(StreamListener):
    k = 0
    """ A listener handles tweets are the received from the stream. """
    def on_status(self, status):
        #if status.coordinates != None:
            try:
                if status.user.location != None:
                    geolocator = Nominatim()
                    location = geolocator.geocode(status.user.location)
                    #print(status.user.location,"=",(location.latitude, location.longitude))
                    print((location.latitude, location.longitude))
            except:
                pass
            self.k+=1
            #print(self.k)
            #print(status.user.location)



    #def on_data(self, data):
        # print received tweet to stdout
    #    print(data)
    #    return True
    def on_error(self, status):
        # print error when data is not correctly
        # received
        print("Error: " + status)
        return True

if __name__ == '__main__':
    # authentication
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # listener instance
    listen = BasicListener()
    # open connection
    geolocator = Nominatim()
    stream = Stream(auth, listen, gzip=True, timeout=None)
    stream.sample()
    #stream.firehose(count=200)