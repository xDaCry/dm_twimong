from connection.mongodb.mongodbConnection import collection
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import time
import sched

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.twitter

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

#Fill the globe with a blue color
map.drawmapboundary(fill_color='aqua')
#Fill the continents with the land color
map.fillcontinents(lake_color='aqua')
map.drawcoastlines()

plt.ion()

plt.show()

#def runX():
result = db.tweets.find({"coordinates":{"$ne" :None}},{"coordinates.coordinates":1,"_id":0})
df = pd.DataFrame(columns=('longitude', 'latitude'))

for x in result:
    df.loc[len(df)] = (x['coordinates']['coordinates'][0],x['coordinates']['coordinates'][1])
    x,y = map(x['coordinates']['coordinates'][0],x['coordinates']['coordinates'][1])
    map.plot(x,y,'ro', markersize=2)
    plt.draw()
