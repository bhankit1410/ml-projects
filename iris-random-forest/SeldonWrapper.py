import pickle
import sklearn

class SeldonWrapper(object):
    def __init__(self):
        with open('model.pickle', 'rb') as pickle_file:
            self._model = pickle.load(pickle_file)

    def predict(self, X, meta=None):
        output = self._model.predict(X)
        return output
