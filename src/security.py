from typing import Optional

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST

import config as config

api_key = APIKeyHeader(name="token", auto_error=False)


def validate_request(header: Optional[str] = Security(api_key)) -> bool:
    if header is None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="API key is missing", headers={}
        )
    if header != config.TOKEN:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Access not allowed", headers={}
        )
    return True
