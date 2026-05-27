import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import os
df = pd.read_csv(fr".\data\ford-specifications.csv")
print(df.head())
print(df.info())
print(df.describe)

num_cols = df.select_dtypes(np.number)
sns.heatmap(num_cols.corr(), annot=True)
plt.figure(figsize=(50, 50))
plt.show()

