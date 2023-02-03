from ..models.User import User
from pymongo import MongoClient, DESCENDING
from werkzeug.security import generate_password_hash
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")

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
