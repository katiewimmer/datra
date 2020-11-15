from sklearn.ensemble import *
from sklearn.datasets import *
from sklearn.model_selection import *
from numpy import *
from sklearn.neural_network import MLPClassifier
from classification_bias import classification_bias
import csv

model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

# load test data
raw_data = open('test_data.csv', 'r')
dataset = list(csv.reader(raw_data, delimiter=','))
x = [row[:-1] for row in dataset]
y = [row[-1] for row in dataset]

features = ["x", "y", "race", "z"] # just a test rn, have to work on it
t = classification_bias(model, x, y, features)
print(t.training_bias())

