import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.User import User as UserModel
from bson import ObjectId
from hashlib import sha224
from Helpers.CollectionFunctions import CollectionFunctions
import uuid

# Taylor is the best


class UserSchema(MongoengineObjectType):
    class Meta:
        model = UserModel
        interfaces = (Node,)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserSchema)
    token = graphene.String()
    error = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    def mutate(self, info, email, password, first_name, last_name):
        collectionFunctions = CollectionFunctions()
        password = sha224(password.encode("utf-8")).hexdigest()
        print(f"Password: {password}")
        user = UserModel(id=ObjectId(), email=email, password=password,
                         first_name=first_name, last_name=last_name)
        user.save()
        user_data = collectionFunctions.findUser(email, password)
        # TODO - is random UUID the best? look at other options
        token = uuid.uuid4().hex
        # TODO - why do I have to use _id.. user_id should work
        collectionFunctions.insert(
            "session", {"sessionID": token, "userID": user_data["_id"], "authenticated": True})
        return CreateUser(user=user, token=token)


class LoginUser(graphene.Mutation):
    token = graphene.UUID()
    error = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        collectionFunctions = CollectionFunctions()
        password = sha224(password.encode("utf-8")).hexdigest()
        user = collectionFunctions.findUser(email, password)
        if user:
            # TODO - is random UUID the best? look at other options
            sessionID = uuid.uuid4().hex
            # TODO - why do I have to use _id.. user_id should work
            collectionFunctions.insert(
                "session", {"sessionID": sessionID, "userID": user["_id"], "authenticated": True})
            return LoginUser(token=sessionID)
        return LoginUser(error="Invalid Login")


class UserInput(graphene.InputObjectType):
    user_id = graphene.String(required=False)
    email = graphene.String(required=False)
    password = graphene.String(required=False)
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserSchema)

    class Arguments:
        changes = UserInput(required=True)
        user_id = graphene.ID(required=True)

    def mutate(self, info, user_id, changes):
        user = UserModel.objects.get(user_id=ObjectId(user_id))
        for k, v in changes.items():
            if k == "password":
                v = sha224(str(v).encode("utf-8")).hexdigest()
            user[k] = v
        user.update(**dict(changes.items()))
        return UpdateUser(user)


class DeleteUser(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        user_id = graphene.ID(required=True)

    def mutate(self, info, user_id):
        user = UserModel.objects.get(user_id=ObjectId(user_id))
        user.delete()
        return DeleteUser(success=True)
