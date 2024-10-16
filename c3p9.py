import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris=pd.read_csv("iriss.csv")
sns.displot(iris['SepalLengthCm'],kde=True,rug=True)
plt.title("Distribution of sepal length")
plt.show()
sns.histplot(iris['PetalWidthCm'],kde=True,bins=20)
plt.title("Histogram of petal width")
plt.show()
sns.replot(x="SepalLengthCm", y="SepalWidthCm", data=iris, bae="species", style="species")
plt.title("sepal length v|s sepal width")
plt.show()