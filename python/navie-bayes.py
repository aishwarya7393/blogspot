import os

import numpy

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfTransformer

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
print(train_data)

clf = MultinomialNB().fit(train_data, categories)

new_article = ["""
Tata Consultancy Services (TCS) on Thursday reported an 8.4 per cent rise in consolidated net profit to Rs 6,586 crore for the second quarter ended September 30 and said uncertainties in environment had resulted in holdbacks in discretionary spend by customers.

The country's largest software services firm had posted a net profit of about Rs 6,073 crore in the year-ago period.

The consolidated revenue grew nearly 8 per cent to Rs 29,284 crore for the said quarter as against Rs 27,165 crore in July-September 2015, the Mumbai-based firm said in a BSE filing.

The figures are as per Indian Accounting Standards (Ind AS).

Shares of the IT major, however, fell by over two per cent today ahead of its second quarter earnings, which were announced after the market hours.

The blue-chip stock went down by 2.17 per cent to end at Rs 2,328.50 on the BSE. During the day, it had slipped 2.44 per cent to Rs 2,323.25.

On the NSE, the stock dipped 2.15 per cent to close at Rs 2,328.90.

Led by the decline in the stock, the company's market valuation fell by Rs 10,166.85 crore to Rs 4,58,814.15 crore.

On the volume front, 3.96 lakh shares of the company changed hands at BSE and over 25 lakh shares were traded on NSE during the day.

TCS CEO and Managing Director N Chandrasekaran termed the second quarter as an "unusual" one for the company.

"Growing uncertainties in the environment are creating caution among customers and resulted in holdbacks in discretionary spending this quarter. In addition, volatility in markets like India and Latin America also muted revenue growth," Chandrasekaran added.

He said the quarter was "good" from a profitability perspective "where despite multiple headwinds, our disciplined approach and focus on operations have helped us deliver a strong margin performance".

"With technology increasingly at the forefront of business, we are confident that this is temporary... Over 180,000 TCSers are now trained with significant expertise in new digital technologies," he said.

Compared with April-June 2016, the company's net profit was up 4.3 per cent, but revenue declined marginally in the said quarter, which is considered to be a strong one for the industry.

During the second quarter, growth was led by life sciences and healthcare, which grew at 4.7 per cent sequentially in constant currency, followed by energy and utilities (up 3.6 per cent.

Europe saw strong growth at 3.7 per cent and Asia-Pacific at 3.5 per cent sequentially in constant currency while North America grew 1.4 per cent sequentially and the UK was flat.

India declined by 7.6 per cent sequentially while Latin America also continued to show volatility, TCS said.

The company announced a total dividend of Rs 6.5 a share.

TCS added 22,665 employees on a gross basis and 9,440 net employees, taking its total headcount to 3.71 lakh as of September 30, 2016.

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

print(s)
test_data = vectorizer.transform(new_article)

predicted = clf.predict(test_data)

print(predicted)


