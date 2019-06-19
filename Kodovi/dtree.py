import pandas as pd
import numpy as np
import sklearn.preprocessing as prep
from sklearn.model_selection import train_test_split, GridSearchCV
import sklearn.metrics as met
from sklearn import tree
from sklearn.metrics import classification_report 

df = pd.read_excel("final_implicit.xlsx") # or explicit

features1 = df.columns[1:2].tolist()
features2 = df.columns[6:].tolist()
features = features1 + features2

#for explicit
#features1 = df.columns[2:3].tolist()
#features2 = df.columns[4:5].tolist()
#features3 = df.columns[6:].tolist()
#features = features1 + features2 + features3

x=df[features]
y=df["sample"]

x_train, x_test, y_train, y_test = train_test_split(  
    x, y, test_size = 0.3, shuffle=True)

dt = tree.DecisionTreeClassifier(max_depth=12)

dt.fit(x_train, y_train)

y_pred = dt.predict(x_test)

accuracy = met.accuracy_score(y_test, y_pred)*100

met.confusion_matrix(y_test, y_pred)

classification_report(y_test, y_pred)
