import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import preprocessing
import sklearn.metrics as met
import numpy as np

df = pd.read_excel("final_implicit.xlsx")

features1 = df.columns[1:2].tolist()
features2 = df.columns[6:].tolist()
features = features1 + features2

x=df[features]
x.columns = features
y=df["sample"]

scaler = preprocessing.StandardScaler().fit(x)
x =pd.DataFrame(scaler.transform(x))
x.columns = features

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, stratify=y)

params = [{'solver':['sgd'],
           'learning_rate':['constant', 'invscaling', 'adaptive'],
           'learning_rate_init':[0.01, 0.005, 0.002, 0.001],
            'activation' : ['identity', 'logistic', 'tanh', 'relu' ],
            'hidden_layer_sizes' : [(10,3), (10,10),],
           'max_iter': [500]
           }]

clf = GridSearchCV(MLPClassifier(), params, cv=5)
clf.fit(x_train, y_train)

print("Izvestaj za test skup:")
y_true, y_pred = y_test, clf.predict(x_test)
cnf_matrix = met.confusion_matrix(y_test, y_pred)
print("Matrica konfuzije", cnf_matrix, sep="\n")
print("\n")

accuracy = met.accuracy_score(y_test, y_pred)
print("Preciznost", accuracy)
print("\n")

class_report = met.classification_report(y_test, y_pred, target_names=clf.classes_)
print("Izvestaj klasifikacije", class_report, sep="\n")

print('Broj iteracija: ', clf.best_estimator_.n_iter_)
print('Broj slojeva: ', clf.best_estimator_.n_layers_)
print('Koeficijenti:', clf.best_estimator_.coefs_, sep='\n')
print('Bias:', clf.best_estimator_.intercepts_, sep='\n')
