import pandas as pd
from sklearn.naive_bayes import  GaussianNB
from sklearn.model_selection import train_test_split
import sklearn.metrics as met
import numpy as np

df = pd.read_excel("Remembered\\final_implicit.xlsx")

features1 = df.columns[1:2].tolist()
features2 = df.columns[6:].tolist()
features = features1 + features2

x=df[features]
y=df["sample"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, stratify=y)

print("GaussianNB")

clf_gnb = GaussianNB()
clf_gnb.fit(x_train, y_train)

y_pred = clf_gnb.predict(x_test)

cnf_matrix = met.confusion_matrix(y_test, y_pred)
print("Matrica konfuzije", cnf_matrix, sep="\n")
print("\n")

accuracy = met.accuracy_score(y_test, y_pred)
print("Preciznost", accuracy)
print("\n")

class_report = met.classification_report(y_test, y_pred, target_names=df["sample"].unique())
print("Izvestaj klasifikacije", class_report, sep="\n")
