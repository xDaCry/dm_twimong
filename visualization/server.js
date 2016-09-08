var webSocketConnections = [];
var nextWebSocketConnectionID = 1;

initServer();

function initServer() {
  var settings = getServerSettingsFromCommandLine();
  createServer(settings);
}

function getServerSettingsFromCommandLine() {
  var parseCommandLineArguments = require('./static/js/command-line-arguments');
  var commandLineArguments = process.argv.slice(2);
  return parseCommandLineArguments(commandLineArguments);
}

function createServer(settings) {
  var createMongoDbConnection = require('./static/js/mongodb-connection');
  var createWebSocketServer = require('./static/js/web-socket-server');
  createMongoDbConnection(broadcastPayload);
  createWebSocketServer(settings.port, serverName(), webSocketConnectionHandler);
}

function broadcastPayload(payload) {
  var stringifiedPayload = JSON.stringify(payload);
  webSocketConnections.forEach(function(webSocketConnection) {
    webSocketConnection.send(stringifiedPayload);
  });
}

function serverName() {
  return 'Twitter Geo Server';
}

function webSocketConnectionHandler(webSocketConnection) {
  addWebSocketConnection();
  addWebSocketDisconnectionListener();

  function addWebSocketConnection() {
    webSocketConnection.id = nextWebSocketConnectionID;
    webSocketConnections[webSocketConnection.id] = webSocketConnection;
    nextWebSocketConnectionID += 1;
    console.log('Client %d connected', webSocketConnection.id);
  }

  function addWebSocketDisconnectionListener() {
    webSocketConnection.on('close', function() {
      delete webSocketConnections[webSocketConnection.id];
      console.log('Client %d disconnected', webSocketConnection.id);
    });
  }
}