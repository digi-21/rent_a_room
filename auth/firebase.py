from firebase_admin import credentials, auth, initialize_app, messaging
from fastapi import FastAPI, Request, Response, HTTPException, Depends, Header
from firebase_admin import auth
from fastapi.security import HTTPBearer
from typing import Dict, Union
from uuid import UUID

cred = credentials.Certificate("/sbrooms-2b842-firebase-adminsdk-pzvbh-9835d17eb8.json")
initialize_app(cred)


#this function can be used for authorization of a parrticular route. It can take a authorization header as a parameter.
#It will also return the firebase user_id which is unique identification for an user along with some decode_claims from firebase.

async def get_current_user(authorization: str = Header(...)) -> str:
    if authorization is None or not authorization.startswith("Bearer "):
        # return an error response if the Authorization header is missing or doesn't use the Bearer scheme
        return {"error": "invalid authorization header"}
    
    #"the authorization token will be look like "Bearer The_token_string" .
    session_token = authorization[7:]

    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        decoded_claims = auth.verify_id_token(session_token)
        user_id = decoded_claims.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid session cookie")
        # user = await get_user_by_id(user_id)
        print(user_id)
        """if not user:
            raise HTTPException(status_code=401, detail="Invalid user ID stored in session")"""
        return {"user_id": user_id, "decoded_claims": decoded_claims}
    except auth.InvalidSessionCookieError:
        raise HTTPException(status_code=401, detail="Invalid session cookie")