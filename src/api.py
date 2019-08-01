from fastapi import APIRouter, Depends

from models import HousingFeatures
from predict import predict
import security

api = APIRouter()


@api.post("/predict")
def post_predict(
    housing_features: HousingFeatures,
    authenticated: bool = Depends(security.validate_request),
):
    assert authenticated
    return predict(housing_features)
