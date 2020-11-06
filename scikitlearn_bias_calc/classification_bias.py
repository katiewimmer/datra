from sklearn.ensemble import *
from sklearn.datasets import *
from sklearn.model_selection import *
from numpy import *

# Currently, I'm thinking there should be three steps:
# One- Check whether each feature (namely race, gender, etc.) is adequately represented in the training set
# Two- Check whether any feature is experiencing a higher number of false positives/false negatives than other features,
#      and output those
# Three- Figure out how I want to visualize my results
class classification_bias:
    def __init__(self, ML_model, class_data, target_vals, features): #ML_model should be scikitlearn machine learning model, class_data should be sample matrix
        self.ml_model = ML_model
        self.class_data = class_data #rows are for each sample, columns are for each feature
        self.target_vals = target_vals #target values of each sample (binary 0 or 1), single dimensional array
        self.features = features #names of the features for each column (think 'race', 'gender', etc. etc.)
    def isStatRep(self, feature, countS, numSamples): #if it's statistically representative (with respect to america)
        if feature == "race":
            race = ["white", "hispanic/latino", "black/african american", "native american", "asian/pacific islander", "other"] #took this off commonly surveyed races, wondering whether categories like hispanic/latino conflate race w ethnicity, e.g. white latinx people
            for i in range (0, len(race)):
                if race[i] in countS: #how to do this for people who identify w more than one race?
                    percentR = countS[race[i]]*1.0/numSamples * 100.0
                    if (race[i] == "white"):
                        if percentR < 65 or percentR > 75:
                            return False
                    if (race[i] == "hispanic/latino"):
                        if percentR < 14 or percentR > 20:
                            return False
                    if race[i] == "black/african american":
                        if percentR < 11 or percentR > 18:
                            return False
                    if race[i] == "native american":
                        if percentR < 1 or percentR > 4:
                            return False
                    if race[i] == "asian/pacific islander": #check these numbers again
                        if percentR < 5 or percentR > 10:
                            return False
        #flesh this out w other features
        elif feature == "sex":
            sex = ["male", "female"] # Census currently only does male and female
            for i in range (0, len(sex)):
                if sex[i] in countS:
                    percentR = countS[sex[i]]*1.0/numSamples * 100.0
                    if (sex[i] == "female"):
                        if percentR < 55 or percentR > 45:
                            return False
                    if sex[i] == "male":
                        if percentR < 55 or percentR > 45:
                            return False
        elif feature == "gender":
            gender = ["cis-male", "cis-female", "transgender"] 
            #Stats said 51.1% female, 48.9% male. Other sources said 0.6% transgender
            #Use what you want, sorry if this isn't what you wanted
            for i in range (0, len(gender)):
                if gender[i] in countS:
                    percentR = countS[sex[i]]*1.0/numSamples * 100.0
                    if (gender[i] == "cis-male"):
                        if percentR < 45 or percentR > 55:
                            return False
                    if gender[i] == "cis-female":
                        if percentR < 47 or percentR > 57:
                            return False
                    if gender[i] == "transgender":
                        if percentR < 0.3 or percentR > 0.9:
                            return False
        elif feature == "age":
            age = ["0-14", "15-64", "65+"] 
            for i in range (0, len(age)):
                if age[i] in countS:
                    percentR = countS[sex[i]]*1.0/numSamples * 100.0
                    if (age[i] == "0-14"):
                        if percentR < 13.5 or percentR > 23.5 :
                            return False
                    if age[i] == "15-64":
                        if percentR < 60 or percentR > 70:
                            return False
                    if age[i] == "65+":
                        if percentR < 11 or percentR > 21:
                            return False
        return True

    def training_bias(self): #step one (refer to top)
        s = [len(self.class_data), len(self.class_data[0])]
        for j in range (0, s[1]):
            countS = {} #count num of samples with specific feature
            for i in range (0, s[0]):
                if self.class_data[i][j] in countS:
                    countS[self.class_data[i][j]] += 1
                else:
                    countS[self.class_data[i][j]] = 0
            b = self.isStatRep(self.features[j], countS, s[1])
            if b is not True:
                return "This dataset is NOT statistically representative of feature: " + self.features[j]
        return "This dataset is statistically representative!!!"


