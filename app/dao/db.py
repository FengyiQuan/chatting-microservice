from ..models.User import User

from pymongo import MongoClient, DESCENDING
from werkzeug.security import generate_password_hash
from bson import ObjectId
import pymongo
import os
import certifi

ca = certifi.where()

uri_srv = os.getenv("MONGODB_URI_SRV", "<NOTSET>")
uri_srv = 'mongodb+srv://Nelson:ruqiulixia0220@cluster0.sprogi7.mongodb.net/test'
try:
    client = MongoClient(uri_srv, tlsCAFile=ca)
except pymongo.errors.ConnectionFailure:
    print("Failed to connect to server {}".format('mongodb://127.0.0.1:27017'))

# print(client)

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")
# rooms_collection = chat_db.get_collection("rooms")
# room_members_collection = chat_db.get_collection("room_members")
messages_collection = chat_db.get_collection("messages")


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    user = users_collection.insert_one({'username': username, 'email': email, 'password': password_hash})
    # print(user)
    return user


def get_user_by_username(username):
    user_data = users_collection.find_one({'username': username})
    # print(user_data)
    return User(str(user_data['_id']), user_data['username'], user_data['email'],
                user_data['password']) if user_data else None


def get_user_by_id(user_id):
    user_data = users_collection.find_one({'_id': ObjectId(user_id)})
    return User(str(user_data['_id']), user_data['username'], user_data['email'],
                user_data['password']) if user_data else None
