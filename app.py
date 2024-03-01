# app.py

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

app = Flask(__name__)

# Load your data and train your models
# ... (Your existing machine learning code)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

# Load your data
data = pd.read_csv("D://well_predictor//t1.csv")

# Separate features and target variables
X = data.drop(columns=['Districts', 'AQ 1 (in metres)', 'Yield(in lps)', 'Drilling Method'], axis=1)
y_depth = data['AQ 1 (in metres)']  # Target variable for depth
y_yield = data['Yield(in lps)']  # Target variable for yield
y_drilling_method = data['Drilling Method']  # Target variable for drilling method

# Split data into training and testing sets
X_train, X_test, y_depth_train, y_depth_test, y_yield_train, y_yield_test, y_drill_train, y_drill_test = train_test_split(
    X, y_depth, y_yield, y_drilling_method, test_size=0.2, random_state=42
)

# Define and train RandomForestRegressor for depth
depth_model = RandomForestRegressor()
depth_model.fit(X_train, y_depth_train)

# Make predictions on the test set for depth
depth_predictions = depth_model.predict(X_test)

# Define and train RandomForestRegressor for yield
yield_model = RandomForestRegressor()
yield_model.fit(X_train, y_yield_train)

# Make predictions on the test set for yield
yield_predictions = yield_model.predict(X_test)

# Define and train RandomForestClassifier for drilling method
drilling_method_model = RandomForestClassifier()
drilling_method_model.fit(X_train, y_drill_train)

# Make predictions on the test set for drilling method
drill_predictions = drilling_method_model.predict(X_test)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input data
        user_input_depth = float(request.form['depth'])
        user_input_features = {}

        # Add code to get input for other features

        # Create a DataFrame for user input
        user_input_df = pd.DataFrame(data={'Depth of Drilling (in metres)': [user_input_depth], **user_input_features})

        # Make predictions using your models
        predicted_depth = depth_model.predict(user_input_df)
        predicted_yield = yield_model.predict(user_input_df)
        predicted_drilling_method = drilling_method_model.predict(user_input_df)

        # Pass the prediction results to the result.html template
        return render_template('result.html', depth=predicted_depth[0], yield_val=predicted_yield[0], drilling_method=predicted_drilling_method[0])

if __name__ == '__main__':
    app.run(debug=True)
