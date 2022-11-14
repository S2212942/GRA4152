## Testing
# 4.1. testerLogistic.py

import argparse
import textwrap

# Initialize the parser
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
         Testing LogisticRegression Class
        ------------------------------------------
        Logistic regression is a linear model for classification.
        Logistic regression is implemented in LogisticRegression class. 
        LogisticRegression contains methods as fit, predict, diagnosis, ...
        This code is used for testing LogisticRegression Class
        '''),
        epilog= textwrap.dedent('''\
        ------------------------------------------
        For more information visit:
        https://github.com/S2212942/GRA4152/tree/main/project'''
        ) )

# Add the parameters positional/ optional
parser.add_argument("--seedValue", help = "provide the seed value which must be an integer ", type = int, default = 1234)

parser.add_argument("--testSize", help = " provide test size which must be a float", type = float, default = 0.3)


parser.add_argument('--covariates', help = "specify the covariates for the model, output data type = list, input string separated by space (e.g. myparser1.py --covariates x1 x2 x3) ", nargs='+')

parser.add_argument('--makePlot', help = "When specified, the plot is created", action=argparse.BooleanOptionalAction)

# Parse the arguments
args = parser.parse_args()
print(args)

randomSeed = args.seedValue # ~ the seed value when splitting the dataset
testSize = args.testSize #  ~ the test size when splitting the dataset
covars = args.covariates # ~ the covariates using for modelling
makePlot = args.makePlot # ~ boolean value that if specifies, makes a plot for logistic model

# One parameter we need to specify when passing the linearModel() method 
# is the string of regression model 
# (for example, y ~ b0 + b1*x1 + b2*x2 + b3*x3)
# Therefore, after input the covariates list using command line, I convert 
# the list to the string model

intercept = "b0" # ~ intercept  for the model
coefs = [] # ~ list of coefficients (eg. ["b1", "b2", "b3"])

# First, Creating the list of coefficients that match with the number of given covariates 
for i in range(1, len(covars)+1):
    coefficienti = "b" + str(i)
    coefs.append(coefficienti)

# Then, Creating the string model
regression = 'y ~ b0'
for coef, covar in zip(coefs, covars):
    a = coef + "*" + covar
    regression += "+ "+ a


# Import Library

import random
import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

from linearmodels import DataSet, LM, LogisticRegression, diagnosticPlot

import statsmodels.api as sm
spector_data = sm.datasets.spector.load()
# if pandas dataset in statsmodels (some versions of statsmodels):
spector_y = spector_data.endog.values
spector_x = spector_data.exog.values
# if numpy arrays in statsmodels (some versions of statsmodels)
#spector_y = spector_data.endog
#spector_x = spector_data.exog

spector = DataSet(spector_x, spector_y)

# Splitting the dataset.
spector.train_test(testSize = testSize, randomState = randomSeed)

## Logistic Regression Model 1

# Creating an instance of the first regression model.
reg1 = LogisticRegression()

# Specifying dataobject, covariates and the training set to use in the
# model.
reg1.linearModel(spector, 'train', regression)

# Fitting the beta parameter's.
reg1.optimize()
reg1.summary()

if makePlot == True:
    # Creating an instance of diagnosticPlot with Linear Regression
    # as input.
    reg1_model_plot = diagnosticPlot(reg1)

    yTe = spector.y_te.reshape(-1,1)
    # Predicting the Logistic Regression 1 model on the test set.
    x_te = spector.x_te
    y_pred = reg1.predict(x_te)
    # Plotting the ROC curve on the test set.
    reg1_model_plot.plot(yTe, y_pred)


#python3 last_exercise.py --testSize 0.3 --covariates x1 x2 x3  --seedValue 1000

 