#python3

'''
This script is used to transform the data into a structure which the model is expecting for the prediction API.
 It will be called under SeldonWrapper.py
'''

import pandas as pd
import os
import re
from sklearn.feature_extraction.text import CountVectorizer

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")


def preprocess_reviews(reviews):
    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]

    return reviews







def transform(inp_list):
    inp_list = preprocess_reviews(inp_list)
    cv = CountVectorizer(binary=True)

