import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PastHires.csv")
# list first 5 rows
newDf = df[['Previous employers','Hired']][5:10]
newDf['Hired'].value_counts().plot(kind='bar')
plt.show()