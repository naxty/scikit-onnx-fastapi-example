from pydantic import BaseModel

import numpy as np


class HousingFeatures(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

    def to_numpy(self):
        return np.array(
            [
                self.CRIM,
                self.ZN,
                self.INDUS,
                self.CHAS,
                self.NOX,
                self.RM,
                self.AGE,
                self.DIS,
                self.RAD,
                self.TAX,
                self.PTRATIO,
                self.B,
                self.LSTAT,
            ]
        ).astype(np.float32)


class PredictionResult(BaseModel):
    predicted: float
