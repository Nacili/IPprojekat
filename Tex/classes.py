i = 0
for item in y:
    if 'LU' in item:
        df["sample"][i] = 'LUNG'
    elif 'HA' in item:
        df["sample"][i] = 'HAEMATOPOIETIC'
    else:
        df = df.drop([i])
    i = i+1
    print(i)