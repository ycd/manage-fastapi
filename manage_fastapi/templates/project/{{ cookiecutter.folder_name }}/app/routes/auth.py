from fastapi import FastAPI, Security, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

router = APIRouter()

security = HTTPBearer()


@router.get("/users/me")
def read_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    return {"scheme": credentials.scheme, "credentials": credentials.credentials}


