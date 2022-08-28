# Automated-Question-Answering-System

## NLP Model for Automated Question Answering in the Field of Data Science and Machine Learning

![2](https://user-images.githubusercontent.com/89520031/172648766-fd04794a-7c00-49d9-8303-aa657e12cab5.png)

# Dataset Explanation:

The dataset was my entire set of experiences regarding different concepts learned from day 1 at Almabetter. 

# Project Summary:

The task was to build a data science related automated question answering model which would retrieve the relevant document and generate the answer for the question.

Did text pre-processing through two different functions: ‘abbreviation_process’ and ‘text_process’.

CountVec ngram model was the final model for question answering due to its excellent performance over LDA, tfidf, word2vec and countvec unigram model. Deployed the final model as streamlit demo in Heroku.

Link:

https://dronademo.herokuapp.com/

This model was structured in such a way so that any fresher can get a complete guideline of asking questions to learn data science and machine learning.

The project is published as python library 'drona' for the benefit of data science and machine learning aspirants. This library will make the learning journey superfast and structured. 

Link: 

https://pypi.org/project/drona/

# Potential Impact and Future Scope:

Generally during the data science learning journey, we do a google search. But 'drona' gives answer within the python environment so that learning and coding can happen in the same place.

As I am simplifying the concepts of data science as a continuous learning process, the same is shared with ‘drona’ for the benefit of the mass.

Day by day, 'drona' will surely make the field of data science more interesting, useful, and simple to more and more data science aspirants

# Installation:

In python environment, you can call 'drona' with following two lines

pip install drona

from drona import tellme

# Use:

You can ask the 'tellme' model of 'drona' any data science and machine learning related question during your learning journey.

e.g.

tellme("What is the role of a data scientist?")
