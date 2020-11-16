# DATRA

DATRA is an open-source library dedicated to increasing the transparency of ML models, specifically those created through Python's sckitlearn library, by calculating and visualizing their biases. 

# Features

Coming soon!

# Installation

Install Datra's dependencies with  either
```python
pip install -U scikit-learn
```
or 
```python
conda install scikit-learn
```

# SciKitLearn

Python's scikitlearn library has dozens of built-in machine learning algorithms and models, titled "estimators". Each estimator can be fitted to some data using its "fit" method.

```
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=0)
X = [[ 1,  2,  3],  # 2 samples, 3 features
... [11, 12, 13]]
y = [0, 1]  # classes of each sample
clf.fit(X, y)
RandomForestClassifier(random_state=0)
```

Once an estimator is fitted, it can also be used for predicting target values of new data.

```
clf.predict(X)
```

This data is usually comes in the format of a design matrix/sample matrix X, which has "n" rows corresponding to n samples and "m" columns corresponding to the m features of your data. For example, a 4 x 2 sample matrix might represent data collected from 4 different people about 2 features, such as race and sex.

There is also usually a target value array y for supervised learning algorithms. In y, there will be n entries (corresponding to n samples) with 'outputs' for each of the samples. In classification models, the entries in y will be integers (e.g. 0 or 1 for binary classification, such as whether someone has a heart condition). In regression models, entries in y will be doubles or floats (e.g. 0.5 for probability).

The goal of DATRA is to test scikitlearn models for bias, both in their datasets and in their accuracy of predictions. "Bias" as currently defined by DATRA is just whether a particular feature or group is overrepresented or underrepresented in a dataset, and whether a particular feature or group results in a higher rate of incorrect classifications such as false positives or false negatives.

Currently, DATRA supports checking training sets against census data to determine whether models including features like "race" are underrepresenting or overrepresenting a particular group. Moving forward, we're adding support for checks for more features and determining bias within prediction accuracy.

# Contributions

Please check out Tasks.md in scikitlearn_calc_bias for stuff I haven't done! I'd love if someone could add more code for a potential feature relating to demographic, like gender etc. in the classification_bias file. 

I also need to add code to make the user input the dataset I'm going to analyze (rather than just making a test one myself), so that would be a super welcome addition! 

# Philosophy

DATRA believes in fostering a welcoming, safe, and meaningfully inclusive environment for those underrepresented in the open-source community. As such, we've made a commitment to moving away from the open-source nomenclature considered offensive or flippant by many marginalized communities. Namely, we refer to our primary branch as "main" rather than "master", and are committed to making any other changes to our nomenclature that would make DATRA feel more welcoming to any of our contributors.
