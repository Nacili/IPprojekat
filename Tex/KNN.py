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