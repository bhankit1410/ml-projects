import pickle
from processing import transform

class Model:
    def __init__(self):
        self._model = pickle.load('../model.pickle')
        self.text = ""

    def predict(self, X, meta=None):
        """
        :param X: The string for analysing the sentiment.
        :param meta: other information
        :return: The output from the prediction of the model in Seldon compliant format
        """
        self.text = X
        output = self._model.predict(X)
        return output
