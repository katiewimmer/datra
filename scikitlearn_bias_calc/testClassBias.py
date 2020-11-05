from sklearn.ensemble import *
from sklearn.datasets import *
from sklearn.model_selection import *
from numpy import *
from sklearn.neural_network import MLPClassifier
from classification_bias import classification_bias

model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
x = [[1, 5, "black/african american", 9], [1, 3, "asian/pacific islander", 15], [1, 4, "white", 18]] #3 samples, 4 features
y = [0, 1, 0]
features = ["x", "y", "race", "z"] # just a test rn, have to work on it
t = classification_bias(model, x, y, features)
print(t.training_bias())




