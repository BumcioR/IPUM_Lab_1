import joblib


def load_model(path="model.joblib"):
    return joblib.load(path)
