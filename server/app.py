from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np
import os

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'bangalore_house_price_prediction.pickle')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load columns
columns_path = os.path.join(os.path.dirname(__file__), 'data_columns.json')
with open(columns_path, 'r') as f:
    data_columns = json.load(f)['data_columns']

location_columns = data_columns[3:]

@app.route('/')
def home():
    return render_template('app.html', locations=location_columns)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        location = data['location']
        sqft = float(data['area'])
        bath = int(data['bath'])
        bhk = int(data['bhk'])

        x = np.zeros(len(data_columns))
        x[0] = bhk
        x[2] = sqft
        x[1] = bath
        

        if location.lower() in [loc.lower() for loc in location_columns]:
            loc_index = next(i for i, col in enumerate(data_columns) if col.lower() == location.lower())
            x[loc_index] = 1

        prediction = model.predict([x])[0]
        return jsonify({'price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
