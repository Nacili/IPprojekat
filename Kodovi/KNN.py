import pandas as pd
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.model_selection import train_test_split
import sklearn.preprocessing as prep
import sklearn.metrics as met


def class_info(clf_arg, x_train_arg, y_train_arg, x_test_arg, y_test_arg):

    clf.fit(x_train_arg, y_train_arg)
    distances, indices = clf.kneighbors(x_test_arg)
    print('distances', distances)
    print('indices', indices)

    y_pred = clf.predict(x_test_arg)

    cnf_matrix = met.confusion_matrix(y_test_arg, y_pred)
    print("Matrica konfuzije", cnf_matrix, sep="\n")
    print("\n")

    accuracy = met.accuracy_score(y_test_arg, y_pred)
    print("Preciznost", accuracy)
    print("\n")

    class_report = met.classification_report(y_test_arg, y_pred, target_names=clf.classes_)
    print("Izvestaj klasifikacije", class_report, sep="\n")

    option = input("Da li zelite informacije o klasifikacije svake instance? (1 za da, 0 za ne)")
    print(option)
    if(option=="1"):
        prediciton_info(x_train_arg, y_train_arg, x_test_arg, y_test_arg, y_pred, indices, distances)



df = pd.read_excel("final_implicit.xlsx")

features1 = df.columns[1:2].tolist()
features2 = df.columns[6:].tolist()
features = features1 + features2

x_original=df[features]

x=pd.DataFrame(prep.MinMaxScaler().fit_transform(x_original))

x.columns = features
y=df["sample"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.95, stratify=y)


k_values = range(3,10)
p_values = [1, 2]
weights_values = ['uniform', 'distance']

for k in k_values:
    for p in p_values:
        for weight in weights_values:
            clf = KNeighborsClassifier(n_neighbors=k,
                                        p=p,
                                        weights=weight)

            print("k="+ str(k))
            print("p="+str(p))
            print("weight=" + weight)

            class_info(clf, x_train, y_train, x_test, y_test)