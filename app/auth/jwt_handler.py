#file responsible for signing, encoding, decoding and returning jWTs

import time
import jwt
from decouple import config 

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


#func returns the generated tokens(jwt)
def token_response(token: str):
    return{
        "access token" : token
    }

#func used to signing the jwt string
def signJWT(userID : str):
    payload = {
        "userID" : userID,
        'expiry': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm = JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
