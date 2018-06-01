# blogspot
A simple blogging web application using communication betwwen two different programming languages. The main blooging application is developed using node.js. It runs a server using the following command from node folder:

node app.js

All the blogs are automatically classified using machine learning classifier. This classification function is provided using a REST API in python flask. This server needs to be running to serve blog classification requests made from the node.js server. Run the flask server using following command from python folder:

python app.py

Thus this web application demonstrates how the data is accessed between APIs built in different environments.
The database used is MongoDB.
