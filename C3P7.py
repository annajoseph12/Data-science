print("SJC22MCA-2007 : ANNA S")
print("Batch : MCA 2023-25")
import pandas as pd
df = pd.read_csv('iriss.csv')
print("Shape of the dataset is : ",df.shape)
print("First 5 and last five rows of data set\n",df)
print("Size of dataset : ",df.size)
print("No. of samples available for each variety\n",df.count())
print("Description of the data set\n",df.describe())