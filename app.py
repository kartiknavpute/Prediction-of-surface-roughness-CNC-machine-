import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return ('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]

    # modify input values to ensure they are within the valid range
    input_data[0] = max(min(input_data[0], 3000), 1000)
    input_data[1] = max(min(input_data[1], 1), 0)
    input_data[2] = max(min(input_data[2], 1), 0)

    input_data = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_data)

    if np.isfinite(prediction):
        return render_template('index.html', prediction_text='Predicted Surface Roughness is {:.3f}'.format(prediction[0]))
    else:
        return render_template('index.html', prediction_text='Prediction Error: Surface roughness could not be predicted.')


if __name__ == "__main__":
    app.run(debug=True)
