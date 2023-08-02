import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))

tokenized_word = word_tokenize(cleaned_text) #Tokenizes the words
# print(tokenized_word)


final_words = []
for word in tokenized_word:
    if word in stopwords.words('english'):
        continue
    else:
        final_words.append(word)

# print(final_words)

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        
        if word in final_words:
            emotion_list.append(emotion)

w  =dict(Counter(emotion_list))

plt.bar(x=w.keys(), height=w.values()) #Shows the Graph of the words
plt.show()

#Sentiment Analysis
def sentiment_analser(senti_text):
    score = SentimentIntensityAnalyzer().polarity_scores(senti_text)
    return score

print(sentiment_analser(cleaned_text)) #returns the sentiment scores for the text

