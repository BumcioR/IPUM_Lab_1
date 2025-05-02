from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model

app = FastAPI()

# model ładowany tylko raz
model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    features = list(request.model_dump().values())  # deprecated method "dict"
    prediction = model.predict([features])[0]
    return PredictResponse(prediction=str(prediction))
