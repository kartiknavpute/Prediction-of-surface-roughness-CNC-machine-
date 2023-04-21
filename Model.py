import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the training data
df = pd.read_excel("finaldata.csv.xlsx")

# Split the data into features (X) and target (y)
X = df[["Spindle_speed", "Feed_rate", "Depth_of_cut"]]
y = df["Surface_Roughness"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train a support vector machine regressor on the training data
regressor = SVR(kernel='linear')
regressor.fit(X_train, y_train)

# Use the trained regressor to make predictions on the test data
y_pred = regressor.predict(X_test)

# Calculate the mean squared error between the actual and predicted values
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print("Mean Squared Error:", mse)
# New data for prediction
new_data = [[1000,0.17,0.4]]
# Make predictions on new data
new_prediction = regressor.predict(new_data)
print('Prediction:',new_prediction)
# New data for prediction
new_data = [[1500,0.160,0.2]]
# Make predictions on new data
new_prediction = regressor.predict(new_data)
print('Prediction:',new_prediction)



import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f, encoding='latin1')



















