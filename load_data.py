from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
import pandas as pd


datafile = "./datasets/diabetes_1.csv"

print("hi")

df = shuffle(pd.read_csv(datafile ,dtype=float))

training_data = df.sample(frac=0.8)
X_training = training_data.drop('Outcome', axis=1).values
Y_training = training_data[['Outcome']].values

testing_data = df.drop(training_data.index)
X_testing = testing_data.drop('Outcome', axis=1).values
Y_testing = testing_data[['Outcome']].values


print(len(df.index))
print(len(training_data.index))
print(len(testing_data.index))

X_scaler = MinMaxScaler(feature_range=(0, 1))
Y_scaler = MinMaxScaler(feature_range=(0, 1))
X_scalered_training = X_scaler.fit_transform(X_training)
Y_scalered_training = Y_scaler.fit_transform(Y_training)

X_scalered_testing = X_scaler.transform(X_testing)
Y_scalered_testing = Y_scaler.transform(Y_testing)
print(X_scalered_training)