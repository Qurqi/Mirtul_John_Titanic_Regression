# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from linear_regression import LinearRegressionModel
from tests import ModelEvaluation
from data_process import clean_data
import numpy as np
import tensorflow as tf


# Load dataset
input_data = pd.read_csv('data/new_data.csv')
# Perform data cleaning
cleaned_data = clean_data(input_data)
# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(cleaned_data.drop('Survived', axis=1), cleaned_data['Survived'], test_size=0.2, random_state=42)

# scale data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Convert train and test data into numpy arrays
print(X_train)
X_train = np.array(X_train, dtype=np.float32)
X_test = np.array(X_test, dtype=np.float32)
y_train = np.array(y_train, dtype=np.float32)
y_test = np.array(y_test, dtype=np.float32)

# Initialize and train model
Mirtul_and_Johns_model= LinearRegressionModel(X_train.shape[1])
Mirtul_and_Johns_model.train_model(X_train, y_train, epochs = 100, lr = 0.01)

# Evaluate model performance
evaluation = ModelEvaluation(Mirtul_and_Johns_model, X_test, y_test)
predictions = Mirtul_and_Johns_model.predict(X_test)

#Save predictions
np.savetxt('predictions.csv', predictions, delimiter=',')

# Compute and display other metrics
mse = evaluation.evaluate_mse()
mae = evaluation.evaluate_mae()
