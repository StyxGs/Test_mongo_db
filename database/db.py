from environs import Env
from pymongo import MongoClient

env: Env = Env()
env.read_env()

connection = MongoClient(
    f'mongodb+srv://{env("NAME_ADMIN")}:{env("PASSWORD_DB")}@cluster0.y1wnqx8.mongodb.net/?retryWrites=true&w=majority')
