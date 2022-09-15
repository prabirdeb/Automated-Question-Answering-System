# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ihSpDvt7UnlZ8dCUKelXhNqg88sTyxPk

**Project: Automated Question-Answering-Streamlit Demo**
"""

# Importing libraries

# Data handling
import numpy as np
import pandas as pd
import re

# machine learning
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Text processing
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string

# Data reading
import pkgutil   # provides binary data
from io import StringIO # for binary to high level data conversion

# from transformers import pipeline
# ques_ans_pipeline = pipeline("question-answering")

# reading the data 
data_science_df_clean=pd.read_csv('data_science_df_clean.csv')

# # reading the data
# bytes_data = pkgutil.get_data(__name__, "data_science_df_clean.csv")

# s=str(bytes_data,'utf-8')
# data = StringIO(s) 
# data_science_df_clean=pd.read_csv(data)

# writing abbreviation processing function
def abbreviation_process(text):
    try:
      abbreviation_dict= {'ml':'machine learning','cnn':'convolutional neural network',
                          'rnn':'recurrent neural network','Sequence Models':'recurrent neural network',
                          'pca':'principal component analysis','svm':'support vector machine',
                          'knn':'k-nearest neighbors','ann':'artificial neural network',
                          'nn':'neural network','sgd':'stochastic gradient descent',
                          'gd':'gradient descent','nlp':'natural language processing',
                          'nlu':'natural language understanding','api': 'application programming interface',
                          'gui':'graphical user interface','mlops': 'ml lifecycle',
                          'lda':'latent dirichlet allocation','svd':'singular value decomposition',
                          'cf':'collaborative filtering','cpu':'central processing unit',
                          'anova':'analysis of variance','auc':'area under the curve',
                          'cv':'cross validation','dnn':'deep neural network',
                          'eda':'exploratory data analysis','gbm':'gradient boosting machine',
                          'glm':'generalized linear model','gru':'gated recurrent unit',
                          'hmm':'hidden marcov model','ica':'independent component analysis',
                          'lstm':'long short term memory','mape':'mean absolute percentage error',
                          'mse':'mean squared error','rmse':'root mean squared error',
                          'nldr':'non-linear dimensionality reduction','r2':'r-squared',
                          'rf':'random forest','roc':'receiver operating characteristic',
                          'ai':'artificial intelligence', 'shap': 'shapley additive explanations',
                          'lime': 'local interpretable model-agnostic explanations', 'eli5': 'explain like I am 5',
                          'xai': 'explainable artificial intelligence', 'opp': 'object oriented programming',
                          'idle': 'integrated development and learning environment', 'sql': 'structured query language',
                          'rdbms' : 'relational database management system', 'iqr': 'interquartile range',
                          'iid': 'independent and indentically distributed', 'clt': 'central limit theorem',
                          'ols': 'ordinary least squares', 'vif': 'variance inflation factor',
                          'xgboost': 'extreme gradient boosting', 'gmlos': 'geometric mean length of stay',
                          'los': 'length of stay', 'smote': 'synthetic minority over-sampling technique',
                          'snn': 'standard neural network', 'brnn': 'idirectional recurrent neural network',
                          'nlg': 'natural language generation', 'bfs': 'breadth first search',
                          'dfs': 'depth first search', 'os': 'operating system',
                          'cvcs' : 'central version control system','dvcs': 'distributed version control system',
                          'wsgi': 'web server gateway interface', 'asgi': 'asynchronous server gateway interface',
                          'mle': 'machine learning engineering', 'gpu': 'graphics processing unit',
                          'dag': 'directed acyclic graph', 'rdd': 'resilient distributed dataset'}
                          
      text = text.lower()    # converting to lowercase
      text= text.replace('?','') # removing '?' mark
      text = [re.sub('\s+', ' ', sent) for sent in text] # Removing new line characters
      text = [re.sub("\'", "", sent) for sent in text] # Removing distracting single quotes
      text=''.join(text)

      for k in text.split():   # loop for replacing the abbreviations
        for i in abbreviation_dict.keys():
          if k==i:
            text=text.replace(k,abbreviation_dict.get(i))
    except:
      text= "Sorry.."

    return text

# writing text pre-processing function
def text_process(text):
    try:
      text = text.lower()    # converting to lowercase
      text =[char for char in text if char not in string.punctuation] # removing punctuations
      text=''.join(text) 
      text=[word for word in text.split() if word not in stopwords.words('english')]  # removing stopwords
      stemmer = SnowballStemmer("english") 
      text=' '.join(text) 
      text = [stemmer.stem(word) for word in text.split()] # stemming operation
      text = ' '.join(text)

    except:
      text= "Please check your statement.."
                      
    return text

# Writing a function for question answering
def tellme(question):
  '''
  This model gives answer to data science related questions.
  '''
  try:
    global data_science_df_clean
    
    # Appending question in the dataset to match the dimension of question and document vector
    data_science_df_clean=data_science_df_clean[(data_science_df_clean.documents!=data_science_df_clean.documents_processed)]
    data_science_df_clean.loc[(data_science_df_clean.index.max()+1)] = text_process(abbreviation_process(question))

    # vectorization of text samples
    document_term_matrix = CountVectorizer(ngram_range=(1,3)).fit_transform(data_science_df_clean.documents_processed.values)

    # CountVec ngram question-answering model
    # Execution time has been reduced tremendously from 2000 ms to 50 ms using cosine similarity of whole matrix, in place of for loop or list comprehension in earlier version
    topic_match=cosine_similarity(document_term_matrix[-1:] , document_term_matrix[:-1])[0] 
    
     
    if topic_match.max()<0.25:  # Deciding the margins through hit and trial for perfect answer
      answer="Sorry ! I have no experience for this question.\n\n::BEGINNERS MAY TYPE 'HELP LINES'"
              
    else:
      answer= data_science_df_clean.documents[np.where(topic_match == topic_match.max())[0][0]]
              
  except:
    answer="I can't understand\n\n::BEGINNERS MAY TYPE 'HELP LINES'"
    
  return answer

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Streamlit Project
import streamlit as st # All the text cell will be displayed after this import statement

st.title("Welcome to 'drona' Data Science and ML Q&A Platform")

quest = st.text_input("Ask your question (BEGINNERS MAY TYPE 'HELP LINES')")
question=quest.title() # .title() is used to get the input question string

ans = tellme(question)

add_bg_from_local('drona.png') 

if(st.button('tellme')):   # display the ans when the submit button is clicked
  st.success(ans)

# pip install streamlit

# !streamlit run streamlit_app.py