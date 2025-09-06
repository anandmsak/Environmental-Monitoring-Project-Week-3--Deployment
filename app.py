import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

# Initialize the flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('models/rf_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the HTML form
    # The order of features must match the order the model was trained on
    feature_values = [float(x) for x in request.form.values()]
    features = [np.array(feature_values)]
    
    # Make a prediction
    prediction = model.predict(features)
    
    # Format the output
    output = round(prediction[0], 2)
    
    # Render the HTML page with the prediction result
    return render_template('index.html', prediction_text=f'Predicted Benzene (C6H6) Concentration: {output} µg/m³')

if __name__ == "__main__":
    app.run(debug=True)