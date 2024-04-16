import pandas as pd
import numpy as np
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Initialize lemmatizer and stemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()



st.title("Text Similarity Analysis")

st.header("Dataset")

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')
df.head()
# df.describe()
df

any_missing_in_columns = df.isnull().any()
st.header("Columns with missing values:")
any_missing_in_columns

st.header("Filling the empty columns")

df['Division Name']=df['Division Name'].fillna(df['Division Name'].mode()[0])

df['Review Text']=df['Review Text'].fillna('.')

df

st.header("Tokenization")

#

def lowercase(text):
    text = text.lower()
    return(text)

def punctuation(text):
    text = re.sub(r'[^\w\s]', '', text)
    return(text)

    
def tokenize(text):
    tokens = word_tokenize(text)
    return(tokens)
    
def stopword(tokens):
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    preprocessed_text = ' '.join(tokens)
    # st.write(preprocessed_text)
    return(preprocessed_text)

def lemmatize(tokens):
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    preprocessed_text = ' '.join(lemmatized_tokens)
    return preprocessed_text

def stem(tokens):
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    preprocessed_text = ' '.join(stemmed_tokens)
    return preprocessed_text

df['lowercase']= df['Review Text'].apply(lowercase)
df['punctuation'] = df['lowercase'].apply(punctuation)
df['tokenized'] = df['punctuation'].apply(tokenize)
df['review_text_preprocessed'] = df['tokenized'].apply(stopword)

st.header("Preprocessed Review Text")

st.write(df['review_text_preprocessed'])

# Apply lemmatization and stemming
df['lemmatized_text'] = df['review_text_preprocessed'].apply(lemmatize)
df['stemmed_text'] = df['review_text_preprocessed'].apply(stem)

st.header("Lemmatized Review Text")
st.write(df['lemmatized_text'])

st.header("Stemmed Review Text")
st.write(df['stemmed_text'])







