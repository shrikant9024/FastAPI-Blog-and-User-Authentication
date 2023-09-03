#verification of the protected route
from fastapi import Request, HTTPException 
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error:bool = True):
        super(jwtBearer,self).__init__(auto_error=auto_Error)

    
    async def __call__(self,request:Request):
        credentials:HTTAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme =="Bearer":
                raise HTTPException(status_code=403,details="Invalid or Expired Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403,details="Invalid or Expired Token")

def verify_jwt(self, jwtoken:str):
    isTokenValid: bool=False 
    payload = decodeJWT(jwtToken)
    if payload:
        isTokenValid = True
    return isTokenValid
