# AI-Well-Water-Predictor
A predictive machine learning model designed to forecast optimal water well depths, expected water yields, and suitable drilling methods for the Balasore district in Odisha, India. This project uses historical well depth data to help optimize water well drilling and improve water resource management.

## Overview
This project builds predictive models using Random Forest techniques to assist in determining the following for water wells:

### Depth of drilling (in meters)
### Expected water yield (in liters per second)
### Recommended drilling method
The dataset used in this project was self-created based on historical data from  National Aquifer Mapping (NAQUIM) and Central Ground Water Board (CGWB) reports. The model is trained on data from 100 districts within Balasore.

## Models Used
1) depthmodel.joblib: Predicts the optimal depth at which to drill.
2) yield_model.joblib: Predicts the expected water yield (in liters per second).
3) drilling_method_model.joblib: Predicts the most suitable drilling method for a given well.

## Algorithms:
1) Random Forest Regressor: Used for predicting the well depth and expected water yield.
2) Random Forest Classifier: Used for predicting the suitable drilling method.

## Features
1)Water Availability Insights: Get predictions on expected water levels in specific locations.

2)Optimized Drilling Methods: Receive recommendations for the best drilling technique to use.

## Prerequisites
Ensure you have the following installed on your machine:

Python 3.x

Flask

Scikit-learn

Pandas

## How to Use
### Clone the repository:
git clone https://github.com/Deepita333/AI-Well-Water-Predictor

### Navigate to the project directory:
cd AI-Well-Water-Predictor

### Install the necessary dependencies:
pip install -r requirements.txt

### Run the Flask app:
python app.py

Open your browser and navigate to http://127.0.0.1:5000/ to start using the AI Well Water Predictor.
<img width="624" alt="image" src="https://github.com/user-attachments/assets/dafab59c-77a7-4200-a4a5-eb0d94f341e0">
![image](https://github.com/user-attachments/assets/f8b53601-06e3-4dbd-bcd4-fbc6d3b811e3)




## Contributing
Feel free to contribute to this project by submitting issues or creating pull requests. Ensure that your code follows best practices and is well-documented.

## License
This project is open-source and available under the MIT License.

