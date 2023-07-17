from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from waifu import WaifuAioClient

from keyboards.inline import sfw_categories_inline_keyboard
from keyboards.inline import waifu_type_inline_keyboard

common_router = Router()


@common_router.message(Command('start'))
async def handle_start(message: Message):
    async with WaifuAioClient() as client:
        sfw_neko: str = await client.sfw(category='neko')
    await message.answer_photo(sfw_neko, reply_markup=sfw_categories_inline_keyboard)
    await message.answer(
        "Привет. Я могу отправить тебе картинки с аниме девочками!! Выбери, что ты хочешь обычные или (18+) картинки.",
        reply_markup=waifu_type_inline_keyboard)