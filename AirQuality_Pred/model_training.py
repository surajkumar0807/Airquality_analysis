# model_training.py

import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

def build_model(X_train, y_train):
    # Define the model
    model = GradientBoostingRegressor()

    # Define hyperparameters grid for tuning
    param_grid = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.1, 0.5],
        'max_depth': [3, 5, 7]
    }

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # Get the best model from grid search
    best_model = grid_search.best_estimator_

    return best_model

def save_model(model, filename):
    # Save the model to a pickle file
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

def load_model(filename):
    # Load the model from the pickle file
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model
