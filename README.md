# Automated-Question-Answering-System

## NLP Model for Automated Question Answering in the Field of Data Science and Machine Learning

![2](https://user-images.githubusercontent.com/89520031/172648766-fd04794a-7c00-49d9-8303-aa657e12cab5.png)

# Summary:

The task was to build a data science related automated question answering model which would retrieve the relevant document and generate the answer for the question.

The dataset was my entire set of experiences regarding different concepts learned from day 1 at Almabetter. Did text pre-processing through two different functions: ‘abbreviation_process’ and ‘text_process’.

CountVec ngram model was the final model for question answering due to its excellent performance over LDA, tfidf, word2vec and countvec unigram model. Deployed the final model as streamlit demo in AWS.

Link:

http://65.2.143.27:8502/

This model was structured in such a way so that any fresher can get a complete guideline of asking questions to learn data science and machine learning.

The project is published as python library 'drona' for the benefit of data science and machine learning aspirants. This library will make the learning journey superfast and structured. 

Link: 

https://pypi.org/project/drona/

# Installation:

In python environment, you can call 'drona' with following two lines

pip install drona

from drona import tellme

# Use:

You can ask the 'tellme' model of 'drona' any data science and machine learning related question during your learning journey.

e.g.

tellme("What is the role of a data scientist?")
