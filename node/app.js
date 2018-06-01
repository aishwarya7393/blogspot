var express=require('express');
var bodyParser = require('body-parser');
var expressSession=require("express-session");

var app=express();
app.set('view engine','ejs');
app.use('/assets',express.static('assets'));
app.use(bodyParser.urlencoded({ extended: true }));

var appcontrol=require('./controllers/appcontrol');

appcontrol(app);

app.listen(7008);
console.log('listening...!!! port 7008');

