# main.py

from data_preprocessing import load_data, drop_columns, replace_missing_values, convert_datetime
from model_training import build_model, save_model
from flask import Flask  # Import Flask from Flask module

app = Flask(__name__)

def main():
    # Load data
    data = load_data("AirQuality.csv")
    
    # Preprocess data
    drop_columns(data)
    replace_missing_values(data)
    data = convert_datetime(data)  # Call the modified convert_datetime function
    
    # Model building
    X = data.drop(columns=['PT08.S1(CO)'])  # Assuming 'PT08.S1(CO)' is the target column
    y = data['PT08.S1(CO)']
    model = build_model(X, y)
    save_model(model, 'model.pkl')
    
    # Run Flask app
    app.run(debug=True)

if __name__ == "__main__":
    main()
