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