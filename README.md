# Crop Yield Prediction Web App

Predict Crop Yields Based on Historical and Environmental Data

Table of Contents
1. Introduction
2. Features
3. Tech Stack
4. Setup Instructions
5. Usage
6. Model Information


Introduction

The Crop Yield Prediction Web App is a machine learning-based tool designed to help farmers, researchers, and agricultural businesses predict crop yields based on historical data and environmental factors like average rainfall, temperature, and pesticide usage. By utilizing advanced machine learning algorithms, this app provides insights into expected yields for various crops across different regions.

Tech Stack

Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Machine Learning: Scikit-learn (Decision Tree Regressor)
Data Processing: Pandas, NumPy
Visualization: Seaborn, Matplotlib
Deployment: Flask web framework


Setup Instructions

Prerequisites:
Python 3.7+
Pip (Python package installer)

Installation:

1. Clone the repository:
   git clone https://github.com/yourusername/crop-yield-prediction.git
   cd crop-yield-prediction

2. Install the required dependencies:
   pip install -r requirements.txt

3. Place your dataset (CSV file) in the root folder.

4. Run the Flask application: python app.py

5. Open your web browser and navigate to http://127.0.0.1:5000/.

Usage

1. Open the app and navigate to the Predict Yield section.
2. Enter the required information:
   - Year
   - Average Rainfall (in mm)
   - Pesticide usage (in tonnes)
   - Average Temperature (in °C)
   - Area (Country)
   - Crop
3.Click the Predict button.
4.The predicted crop yield will be displayed on the screen.

Model Information

The app uses a Decision Tree Regressor model, which was trained on historical crop yield data. Environmental and geographical factors such as rainfall, pesticide usage, and temperature are also included in the prediction model.

Input Features: Year, Average Rainfall, Pesticides, Average Temperature, Area, Crop.
Output: Crop Yield (in hg/ha).
The trained model files (dtr.pkl, preprocessor.pkl) are loaded when the Flask app runs.

