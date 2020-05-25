# Sentiment-Analysis on IMDB movies with Sci-kit Learn.


## Steps to be followed:

#### --> Introduction and Importing the Data
#### --> Transforming Documents into Feature Vectors
#### --> Term Frequency-Inverse Document Frequency (TF-IDF)
#### --> Calculate the TF-IDF of the Term 'Is'
#### --> Data Preparation
#### --> Tokenization of Documents
#### --> Document Classification Using Logistic Regression
#### --> Load Saved Model from Disk
#### --> Model Accuracy

## Steps to deploy:

#### Build Docker image
    $ docker build -t imdb_sentiment:0.0.1 .
 
### Start the seldon-core model
    $ docker run --env-file dev.properties -p 5000:5000 -it imdb_sentiment:0.0.1
    