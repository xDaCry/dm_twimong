var MongoClient = require('mongodb').MongoClient;

function createMongoDbConnection(payloadCallback) {
  startFileringGeocodedTweets();

  function startFileringGeocodedTweets() {
    var url = 'mongodb://localhost:27017/twitter';

    MongoClient.connect(url, function(err, db) {
        console.log("Connected correctly to server");

    var col = db.collection('tweets');
    var stream = col.find({},{tailable:true}).stream();

    stream.on('error', function (err) {
      console.error(err)
    });

    stream.on('data', function (doc) {
      var payload = buildPayload(doc);
      if (payload) {
        payloadCallback(payload);
      }
    })});
  }
}

function buildPayload(doc) {
  return doc;
}

module.exports = createMongoDbConnection;
