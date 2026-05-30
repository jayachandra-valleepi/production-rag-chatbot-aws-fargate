import time
import jwt

SECRET_KEY = "mysecretkey"


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(username: str):

    payload = {
        "username": username,
        "expires": time.time() + 6000
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token_response(token)


def decode_jwt(token: str):

    try:
        decoded_token = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return decoded_token if decoded_token["expires"] >= time.time() else None

    except:
        return {}