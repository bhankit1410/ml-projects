import pickle


class Model:
    def __init__(self):
        self._model = pickle.load('model.pickle')

    def predict(self, X):
        output = self._model.predict(X)
        return output
