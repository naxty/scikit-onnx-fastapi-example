from fastapi import APIRouter, Depends

from models import HousingFeatures, PredictionResult
from predict import predict
import security

api = APIRouter()


@api.post("/predict", response_model=PredictionResult)
def post_predict(
    housing_features: HousingFeatures,
    authenticated: bool = Depends(security.validate_request),
):
    assert authenticated == True
    return predict(housing_features)
