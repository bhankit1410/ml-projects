#author: Ankit bhardwaj
"""
This class is to wrap the model into Seldon and deploy it on kubernetes using a dockerfile
"""

import pickle
from preprocessing import from_file


class SeldonWrapper:
    def __init__(self):
        with open('mnist.pickle', 'rb') as r:
            self.model = pickle.load(r)
        r.close()


def predict(self, X, meta=None):
    """

    :param self:
    :param X: if meta None, X is list of features
    :param meta: {"path":"path/to/csv"}
    :return:
    """
    print(f'predict called')
    if meta:
        x = from_file(meta['path'])
    else:
        x = X
    print(x[1])
    return self.model.predict(X)
