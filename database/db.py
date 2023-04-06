from environs import Env
from motor import motor_asyncio

env: Env = Env()
env.read_env()

connection = motor_asyncio.AsyncIOMotorClient(
    f'mongodb+srv://{env("NAME_ADMIN")}:{env("PASSWORD_DB")}@cluster0.y1wnqx8.mongodb.net/?retryWrites=true&w=majority')
