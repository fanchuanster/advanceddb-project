from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
import pandas as pd


datafile = "./datasets/diabetes_1.csv"

print("hi")

df = shuffle(pd.read_csv(datafile))

training_data = df.sample(frac=0.8)
test_data = df.drop(training_data.index)

print(len(df.index))
print(len(training_data.index))
print(len(test_data.index))