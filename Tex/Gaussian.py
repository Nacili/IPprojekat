features1 = df.columns[1:2].tolist()
features2 = df.columns[6:].tolist()
features = features1 + features2

x = df[features]
y = df["sample"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, stratify=y)

clf_gnb = GaussianNB()

clf_gnb.fit(x_train, y_train)

y_pred = clf_gnb.predict(x_test)