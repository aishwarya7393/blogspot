import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction import DictVectorizer

from nltk.tokenize import word_tokenize

Dv = DictVectorizer()
vectorizer = CountVectorizer(stop_words="english",lowercase=True)
import os
email_list = []

for name1 in os.listdir("Data"):
    arr = ""
    for name in os.listdir("Data/"+name1):
        fl = open("Data/"+name1+"/"+name,"r")
        arr += fl.read()
    email_list.append(arr)

bag_of_words = vectorizer.fit_transform(email_list)

categories = ['Business/Economy','Entertainment','Health','Political','Sports','Technology/Science']
##hello = bag_of_words.toarray()

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(bag_of_words)
X_train_tf = tf_transformer.transform(bag_of_words)

##print(X_train_tf.toarray())

##bag_of_words = vectorizer.transform(email_list)

##print (bag_of_words)

##print (vectorizer.vocabulary_.get('great'))

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(bag_of_words)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X_train_tfidf, categories)

from sklearn.naive_bayes import GaussianNB
clf1 = GaussianNB()
clf1.fit(X_train_tfidf.toarray(),categories)

from sklearn.naive_bayes import BernoulliNB
clf2 = BernoulliNB()
clf2.fit(X_train_tfidf,categories)

from sklearn.linear_model import LogisticRegression
clf3 = LogisticRegression()
clf3.fit(X_train_tfidf,categories)

new_article = ["""
The singer Will Young has announced he has left the latest series of Strictly Come Dancing for personal reasons.

The 37-year-old said: “I leave with joy in my heart that I have been able to take part in one of the most loved shows on British television.

“To be a part of Strictly has been a long-time ambition of mine. As a performer, a viewer, and a fan of the show, to dance as a contestant was an experience I always hoped for. I have made some great friends, and am in awe of their performances week in, week out.”

He praised his dancing partner, Karen Clifton, saying that the creative partnership with her had been “the most wonderful thing” and he was “eternally grateful to her for her direction, talent and guiding me through three wonderful dances that I will be able to show my grandkids in years to come”.
Young thanked everyone involved with the top-rating BBC1 show “from the bottom of my heart”, as well as the BBC.


The stories you need to read, in one handy email
 Read more
“I wish my compatriots so much luck, and although I am back to being a viewer again, I’m certainly going to ‘keeeep dancing’!”

The BBC said: “Due to personal reasons, Will Young has decided to withdraw from Strictly Come Dancing. The show fully respects his decision and wishes him all the best for the future.”

Earlier on Tuesday, the BBC had to defend its hit show after the departure of the second black contestant in as many weeks prompted accusations of racism.

Young and Clifton were in joint fourth position on the leaderboard with 31 points.

They performed a salsa during last weekend’s movie-themed episode, but drew criticism from the head judge, Len Goodman.

Young clashed with Goodman after the judge told the pair he thought there was a lack of salsa in the dance. Their exchange ended with Goodman telling Young to “turn up, keep up, shut up”.

An insider denied there was any ill feeling between dancer and judge after the spat, adding there was much mutual respect between them.

Young and Clifton had been due to perform the Viennese waltz to Say Something, by A Great Big World and Christina Aguilera, on Saturday night. The show will proceed as normal with a results show on Sunday, when the third celebrity will be eliminated after the public vote.

Strictly is not Young’s only BBC primetime appearance. In March 2012 he was on the panel for a Question Time debate about gay marriage and he has made several appearances on Top of the Pops. Young’s music career began in earnest when he won the first series of the ITV talent show Pop Idol in 2002.



"""]

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

X_new_counts = vectorizer.transform(new_article)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

print(clf.predict(X_new_counts))
pre = clf.predict_proba(X_new_counts)
print(pre)

##for doc, category in zip(docs_new, predicted):
##     print('%r => %s' % (doc, twenty_train.target_names[category]))

print(clf1.predict(X_new_counts.toarray()))
pre1 = clf1.predict_proba(X_new_counts.toarray())
print(pre1)

print(clf2.predict(X_new_counts))
pre2 = clf2.predict_proba(X_new_counts)
print(clf2.predict_log_proba(X_new_counts))
print(pre2)

print(clf3.predict(X_new_counts))
pre3 = clf3.predict_proba(X_new_counts)
print(pre3)


import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

objects = ('Buss/Eco','Enter','Health','Political','Sports','Tech/Sci')
y_pos = np.arange(len(objects))
performance =[]
performance1 =[]
performance2 =[]
performance3 =[]

for i in pre[0]:
    performance.append(i)
for i in pre1[0]:
    performance1.append(i)
for i in pre2[0]:
    performance2.append(i)
for i in pre3[0]:
    performance3.append(i)

y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)
plt.subplot(221)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Score')
plt.title('MultinomialNB')

plt.subplot(222)
plt.bar(y_pos, performance1, align='center', alpha=0.5,color='y')
plt.xticks(y_pos, objects)
plt.ylabel('Score')
plt.title('GaussianNB')


plt.subplot(223)
plt.bar(y_pos, performance2, align='center', alpha=0.5,color='black')
plt.xticks(y_pos, objects)
plt.ylabel('Score')
plt.title('BernoulliNB')

plt.subplot(224)
plt.bar(y_pos, performance3, align='center', alpha=0.5,color='r')
plt.xticks(y_pos, objects)
plt.ylabel('Score')
plt.title('Maximum Entropy')

plt.show()
