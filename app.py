from flask import Flask, request, render_template
import pandas as pd
import pickle

# Loading models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Creating Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        Year = int(request.form['Year'])
        average_rain_fall_mm_per_year = float(request.form['average_rain_fall_mm_per_year'])
        pesticides_tonnes = float(request.form['pesticides_tonnes'])
        avg_temp = float(request.form['avg_temp'])
        Area = request.form['Area']
        Item = request.form['Item']

        # Create a DataFrame of input features to match the columns expected by the preprocessor
        input_data = pd.DataFrame([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]],
                                  columns=['Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'Area', 'Item'])

        # Transform the input features using the preprocessor
        transformed_features = preprocessor.transform(input_data)

        # Make the prediction
        predicted_value = dtr.predict(transformed_features)[0]  # Get the predicted value

        # Render the form.html with the predicted value
        return render_template('form.html', predicted_value=predicted_value)

    return render_template('form.html')  # Show the form if GET request

if __name__ == '__main__':
    app.run(debug=True)
