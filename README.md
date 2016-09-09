# dm_twimong - Having fun with the twitter API

Welcome people to joining my idea of data mining the twitter data given by their API. <br />
This project was initiated by having own interest in this subject, aswell as creating a project for a seminar at university.

=============
### The goal of this project is:

- [x] Collecting data from twitter streams
- [x] Store the data in a MongoDB (NoSQL)
- [x] Analyze the data for different scenarios (language, hashtags etc.)
- [x] Visualize the data stored /javascript
- [ ] make it pretty!
 
=============
### The project is seperated in different packages:

> **anaylze**: This package includes all the queries for analyzing the data stored in databases,

> **connection**: This package includes all the classes for creating connections to databases and the twitter stream.

> **visualization**: This package includes all the classes for visualizing the data stored (Javascript based including D3.js, AngularJs and Websocket)

=============
### How to start the programm:

- [x] Install MongoDB (db : 'twitter' , collection : 'tweets' , cappedCollection : True)
- [x] Install Node.js
- [x] Start MongoDB
- [x] Start the websocket server as shown in [1]
- [x] Start the http-server as shown in [2]
- [x] Start the streamer.py
- [x] Go to http://localhost:8000 to see the visualization

## [1] - Start websocket server:

- Start Node.js command prompt
- Direct the cursor to ../dm_twimong/visualization
- npm start


## [2] - Start http-server:

- Start Node.js command prompt
- Direct the cursor to ../dm_twimong/visualization
- http-server -p 8000
