from flask import Flask, render_template, url_for, request, session, redirect
import operator
from operator import itemgetter
import csv
import sys
import datetime
from flask import jsonify
import os
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfTransformer
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = "todo"
#app.config['MONGO_URI'] = "mongodb://sh221:sh221@ds129344.mlab.com:29344/todo"
#app.config['MONGO_URI'] = "localhost:44444/blogapp"
app.config['SECRET_KEY']='blogs1234'

@app.route('/',methods=['GET','POST'])
def index():
    if(request.method=='GET'):
        return jsonify({'string':'Hello world'})
    else:
        #print(request.data)
        print(request.get_json());
        obj=request.get_json();
        text=obj['article'];
        predicted= classify(text);
        return jsonify({'predicted':predicted[0]})
    
    
@app.route('/classify')
def classify(input_article):
    ALL_Docs = []

    categories = ['Business/Economy','Entertainment','Health','Political','Sports','Technology/Science']

    for folder in os.listdir("Data"):
        article = ""
        for filename in os.listdir("Data/"+folder):
            fl = open("Data/" + folder + "/" + filename, "r")
            read = fl.read()
            article += read
        ALL_Docs.append(article)


    vectorizer = CountVectorizer(stop_words="english",lowercase=True)

    train_data = vectorizer.fit_transform(ALL_Docs)
    #print(train_data)

    clf = MultinomialNB().fit(train_data, categories)
    new_article = [input_article]
    fl = open("stop words.txt","r")
    arr = []
    for w in fl.readlines():
        arr.append(w.rstrip('\n'))

    s =""

    tokens = word_tokenize(new_article[0])
    for w1 in tokens:
        w =w1.lower()
        if w not in arr:
            s = s + " " + w
    new_article[0] = s

    print(s)
    test_data = vectorizer.transform(new_article)

    predicted = clf.predict(test_data)

    print(predicted)
    return predicted

if __name__ == '__main__':
    app.secret_key = 'mysecretkey'
    app.run(debug=False)