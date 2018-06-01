import numpy as np
import lda
from sklearn.decomposition import LatentDirichletAllocation

from sklearn.feature_extraction.text import CountVectorizer

from nltk.tokenize import word_tokenize

n_features = 10000
n_topics = 6
n_top_words = 300
vectorizer = CountVectorizer(max_df=0.95, min_df=2,max_features=n_features,stop_words='english')

import os

path = 'D:/Project/lda'

email_list = []
for name1 in os.listdir("Data"):
    for name in os.listdir("Data/"+name1):
        fl = open("Data/"+name1+"/"+name,"r")
        email_list.append(fl.read())

bag_of_words = vectorizer.fit_transform(email_list)

clf  = lda.LDA(n_topics=n_topics, n_iter=1000,random_state=0)

clf.fit(bag_of_words)

categories = vectorizer.get_feature_names()

topic_word = clf.topic_word_  # model.components_ also works

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(categories)[np.argsort(topic_dist)][:-n_top_words:-1]
    fw = open("D:/Project/lda/"+ str(i) + ".txt", "w")
    count = topic_words.tolist()
    ar = []
    for j in count:
        ar.append(str(j))
    for j in ar:
        fw.write("%s\n" % j)
    fw.close()


k = 0
ans = []

doc_topic = clf.doc_topic_
for name1 in os.listdir("Tt"):
    con0 = 0;con1 = 0;con2 = 0;con3 = 0;con4 = 0;con5 = 0
    ans1 = []
    for name in os.listdir("Tt/"+name1):
        str = name
        n = ""
        for i in range(len(str)):
            if str[i] == '.':
                break
            n=n+str[i]
        if doc_topic[int(n)].argmax() == 0:
            con0 +=1
        elif doc_topic[int(n)].argmax() == 1:
            con1 += 1
        elif doc_topic[int(n)].argmax() == 2:
            con2 +=1
        elif doc_topic[int(n)].argmax() == 3:
            con3 +=1
        elif doc_topic[int(n)].argmax() == 4:
            con4 +=1
        else :
            con5 +=1
    ans1.append(con0);ans1.append(con1);ans1.append(con2);ans1.append(con3);ans1.append(con4);ans1.append(con5)
    ans.append(ans1)
print(ans)

