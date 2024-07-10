from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

simple_api = FastAPI()


class User(BaseModel):
    name: str
    email: str


users = {}


@simple_api.get('/')
def home() -> Dict[str, int]:
    """Return len users"""
    return {'Users': len(users)}


@simple_api.get('/users/{user_id}')
def get_users(user_id: int) -> Dict[str, str]:
    """Return specific user"""
    if user_id not in users:
        return {'Error': 'User not found'}
    return users[user_id]


@simple_api.post('/users')
def post_users(user: User, user_id: int) -> Dict[str, str]:
    """Post new user"""
    if user_id not in users:
        users[user_id] = {'name': user.name, 'email': user.email}
        return {'Success': 'User added'}
    return {'Error': 'User already exists'}
