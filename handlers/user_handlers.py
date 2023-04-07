import json

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.db import connection
from services.service import aggregate_salaries, check_valid_str

router = Router()


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    name_user: str = message.from_user.first_name
    await message.answer(f'Привет, {name_user}!')


@router.message(F.text)
async def info_search(message: Message) -> None:
    data: dict | bool = await check_valid_str(message.text)
    if data:
        answer: dict = await aggregate_salaries(data['dt_from'], data['dt_upto'], data['group_type'], connection)
        await message.answer(json.dumps((answer)))
    else:
        await message.answer('Данные не действительны!')
