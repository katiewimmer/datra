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
            race = ["white", "hispanic/latino", "black/african american", "native american", "asian/pacific islander", "other"] 
            #took this off commonly surveyed races, wondering whether categories like hispanic/latino conflate race w ethnicity, e.g. white latinx people
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
        elif feature == "distribution of net wealth in the US":
        #Stats used from statista.com
        #Stats said that 30.5% of the net wealth in the US is from the Top 1%, 38.5% is from the 90th to 99th Percentile, 28.7% is from the 50th to 90th Percentile, and 1.8% is from the Bottom 50 Percent
            wealth = ["Top 1%", "90th to 99th Percentile", "50th to 90th Percentile", "Bottom 50% Percentile"] 
            for i in range (0, len(wealth)):
                if wealth[i] in countS:
                    percentR = countS[sex[i]]*1.0/numSamples * 100.0     
                    if (wealth[i] == "Top 1%"):
                        if percentR < 28.5 or percentR > 32.5:
                            return False 
                    if (wealth[i] == "90th to 99th Percentile"):
                        if percentR < 35 or percentR > 43:
                            return False 
                    if (wealth[i] == "50th to 90th Percentile"):
                        if percentR < 25.5 or percentR > 33:
                            return False 
                    if (wealth[i] == "Bottom 50% Percentile"):
                        if percentR < 1 or percentR > 4:
                            return False
        elif feature == "disability and functioning":
        #Stats used from cdc.gov 
        #Stats said that for adults aged 18 and over- 16.5% face Hearing Trouble, 12.9% face Vision Trouble, 7.8% are unable to/find it difficult to walk a quarter mile, 16.3% face any physical functioning difficulty 
        #"Level of reported difficulty in 6 domains of functioning" is NOT INCLUDED BELOW
            difficulty = ["Hearing trouble", "Vision Trouble", "Unable/Difficult to walk quarter mile", "Any physical functioning difficulty"]
            for i in range (0, len(difficulty)):
                percentR = countS[sex[i]]*1.0/numSamples * 100.0
                if (difficulty[i] == "Hearing Trouble"):
                    if percentR < 12.5 or percentR > 19.5:
                        return False 
                if (difficulty[i] == "Vision Trouble"):
                    if percentR < 10.5 or percentR > 14:
                        return False 
                if (difficulty[i] == "Unable/Difficult to walk quarter mile"):
                    if percentR < 5.5 or percentR > 9.5:
                        return False 
                if (difficulty[i] == "Any physical functioning difficulty"):
                     if percentR < 13.5 or percentR > 19:
                         return False 
        elif feature == "education attainment":
            education = ["High School or equivalent degree", "Some college, no degree", "Associates degree", "Bachelors degree", "Graduate or professional degree"]
            for i in range(0, len(education)):
                percentR = countS[sex[i]]*1.0/numSamples * 100.0
                if (education[i] == "High School or equivalent degree"):
                    if percentR < 15.5 or percentR > 30.0:
                        return False
                if (education[i] == "Some college, no degree"):
                    if percentR < 15.0 or percentR > 20.0:
                        return False
                if (education[i] == "Associates degree"):
                    if percentR < 3.0 or percentR > 12.0:
                        return False
                if (education[i] == "Bachelors degree"):
                    if percentR < 15.0 or percentR > 25.0:
                        return False
                if (education[i] == "Graduate or professional degree"):
                    if percentR < 8.0 or percentR > 15.5:
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


