from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.svm import SVR
# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the Flask app
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    # Extract the request data
    data = request.get_json(force=True)

    # Extract the input features
    spindle_speed = float(data['Spindle_speed'])
    feed_rate = float(data['Feed_rate'])
    depth_of_cut = float(data['Depth_of_cut'])

    # Make a prediction using the trained model
    prediction = model.predict([[spindle_speed, feed_rate, depth_of_cut]])

    # Return the predicted value as a JSON response
    return jsonify({'Surface_Roughness': prediction.tolist()[0]})
if __name__ == '__main__':
    app.run(debug=True)
import requests

url = 'http://localhost:5000/predict'
data = {
    'Spindle_speed': 2000,
    'Feed_rate': 0.18,
    'Depth_of_cut': 0.2
}
response = requests.post(url, json=data)
print(response.json())
