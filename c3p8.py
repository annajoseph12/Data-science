import pandas as pd
import seaborn
import matplotlib.pyplot as plt
df=pd.read_csv('iriss.csv')
seaborn.pairplot(df,kind='scatter')
seaborn.pairplot(df,kind='kde')
seaborn.pairplot(df,kind='hist')
seaborn.pairplot(df,kind='reg')
plt.show()
