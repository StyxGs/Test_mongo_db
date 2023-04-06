import json

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.db import connection
from services.service import aggregate_salaries

router = Router()


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer('Привет!')


@router.message(F.text)
async def info_search(message: Message) -> None:
    data: dict = json.loads(message.text)
    answer: list = await aggregate_salaries(data['dt_from'], data['dt_upto'], data['group_type'], connection)
    await message.answer(str(answer))
