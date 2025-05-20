import os
import joblib

def map_gender(X):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    gender_map_path = os.path.join(base_dir, "gender_map.pkl")
    gender_map = joblib.load(gender_map_path)
    X = X.copy()
    X['gender'] = X['gender'].map(gender_map)
    return X