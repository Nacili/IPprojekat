import pandas as pd
import numpy as np
from pandas import ExcelWriter

df = pd.read_excel("Remembered/EXTRACTED_CLASSES_binded.xlsx", "Sheet1")

y = df["sample"]

i = 0
for item in y:
    if 'LU' in item:
        df["sample"][i] = 'LUNG'
    elif 'HA' in item:
        df["sample"][i] = 'HAEMATOPOIETIC'
    else:
        df = df.drop([i])
    i = i+1

writer = ExcelWriter(r'Remembered/final_implicit.xlsx')
df.to_excel(writer,'Sheet1', index=False)
writer.save()

    
