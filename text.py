import pandas as pd
import numpy as np
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

df = pd.read_excel("C:\\Users\\aparn\\Desktop\\AI\\chatbot\\chats.xlsx")
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    preprocessed_text = ' '.join(words)
    
    return preprocessed_text

def tolower_text(text):
    text = text.lower()
    return text

df['text'] = df['text'].apply(preprocess_text)
df['intent'] = df['intent'].apply(tolower_text)

text = ' '.join(df['text'])
words_arr = text.split()
unique_words = set(words_arr)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['text'])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out() )

classifier = SVC()
X_train = tfidf_df
y_train = df.iloc[:,-1]
classifier.fit(X_train, y_train)

def give_intent(words):
    words = preprocess_text(words)
    input_msg = ' '.join([word for word in words.split() if word in unique_words])
    if len(input_msg)==0:
        return "NULL"
    data = df.iloc[:,[0]]
    dnew_row = pd.DataFrame([input_msg], columns=['text'])
    data = pd.concat([data, dnew_row], ignore_index=True)
    vectorizer = TfidfVectorizer()
    new_tfidf_matrix = vectorizer.fit_transform(data['text'])
    new_tfidf_df = pd.DataFrame(new_tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out() )
    prediction = classifier.predict(new_tfidf_df.iloc[[-1],:])
    return prediction[0]









