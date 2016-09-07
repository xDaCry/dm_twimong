import tweepy
import matplotlib.animation as animation
from connection.mongodb.mongodbConnection import collection
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from connection.twitter.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        #post = collection.insert_one(status._json).inserted_id
        #print(post)
        self.get_tweet(status)

    # Twitter error list : https://dev.twitter.com/overview/api/response-codes

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

    @staticmethod
    def get_tweet(tweet):
        if tweet.coordinates is not None:
            print(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            x, y = map(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            map.plot(x, y, 'ro', markersize=2)
            plt.draw()


#def start_stream():
if __name__ == '__main__':

    # Set a title
    plt.title("Tweet's around the world")

    # Declare map projection, size and resolution
    map = Basemap(projection='merc',
                  llcrnrlat=-80,
                  urcrnrlat=80,
                  llcrnrlon=-180,
                  urcrnrlon=180,
                  lat_ts=20,
                  resolution='l')

    #map.bluemarble(scale=1)

    # Set interactive mode ON
    plt.ion()

    # Display map
    plt.show()

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