import json
from bson import ObjectId
from flask import Response, request
from flask_restful import Resource
import uuid
from hashlib import sha224
from Helpers.CollectionFunctions import CollectionFunctions

class RegisterRequests(Resource):
    def post(self):
        collectionFunctions = CollectionFunctions()
        print(request.json)
        email = request.json["email"]
        password = sha224(request.json["password"].encode("utf-8")).hexdigest()
        first_name = request.json["firstName"]
        last_name = request.json["lastName"]
        token = None
        if not collectionFunctions.findUser(email):
            user = {"email": email, "password": password, "first_name": first_name, "last_name": last_name}
            collectionFunctions.insert("User", user)
            user = collectionFunctions.findUser(email)
            token = uuid.uuid4().hex
            session = {"sessionID": token, "userID": user["_id"], "authenticated": True}
            collectionFunctions.insert(
                "session", session)
            for key in session:
                if isinstance(session[key], ObjectId):
                    session[key] = str(session[key])
            return Response(json.dumps(session))
        return Response(json.dumps({"error": "Email has already registered"}), status=400)

class LoginRequests(Resource):
    def get(self, token=None):
        collectionFunctions = CollectionFunctions()
        session = collectionFunctions.get_session(token)
        if session:
            for key in session:
                if isinstance(session[key], ObjectId):
                    session[key] = str(session[key])
            return Response(json.dumps(session), mimetype="application/json")
        return Response(json.dumps({"error": "Invalid Token"}), mimetype="application/json", status=400)

    def post(self):
        collectionFunctions = CollectionFunctions()
        print(request.json)
        email = request.json["email"]
        password = sha224(request.json["password"].encode("utf-8")).hexdigest()
        token = None
        user = collectionFunctions.validateLogin(email, password)
        if user:
            token = uuid.uuid4().hex
            session = {"sessionID": token, "userID": user["_id"], "authenticated": True}
            collectionFunctions.insert(
                "session", session)
            for key in session:
                if isinstance(session[key], ObjectId):
                    session[key] = str(session[key])
            return Response(json.dumps(session))
        return Response(json.dumps({"error": "Invalid Login"}), status=400)
