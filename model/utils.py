def map_gender(X):
    import joblib
    gender_map = joblib.load("model/gender_map.pkl")
    X = X.copy()
    X['gender'] = X['gender'].map(gender_map)
    return X