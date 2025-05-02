from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    data = load_iris()
    return data.data, data.target


def train_model(X, y):
    clf = RandomForestClassifier()
    clf.fit(X, y)
    return clf


def save_model(model, path="model.joblib"):
    joblib.dump(model, path)


if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)
    print("Model trained and saved.")
