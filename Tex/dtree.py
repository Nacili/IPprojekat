features1 = df.columns[1:2].tolist()
features2 = df.columns[6:].tolist()
features = features1 + features2

x = df[features]
y = df["sample"]

x_train, x_test, y_train, y_test = train_test_split(  
    x, y, test_size = 0.3, shuffle=True)
    
dt = tree.DecisionTreeClassifier(max_depth=12)
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
