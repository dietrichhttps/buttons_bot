from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import dog_cucumber_keyboard, remove_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    print('Апдейт дошел до хэндлера process_start_command')
    await message.answer(
        text=LEXICON_RU['answers']['/start'],
        reply_markup=dog_cucumber_keyboard
    )


@router.message(F.text == LEXICON_RU['buttons']['dog'])
async def process_dog_answer(message: Message):
    print('Апдейт дошел до хэндлера process_dog_answer')
    await message.answer(
        text=LEXICON_RU['answers']['if_dog'],
        reply_markup=remove_keyboard
    )


@router.message(F.text == LEXICON_RU['buttons']['cucumber'])
async def process_cucumber_answer(message: Message):
    print('Апдейт дошел до хэндлера process_cucumber_answer')
    await message.answer(
        text=LEXICON_RU['answers']['if_cucumber'],
        reply_markup=remove_keyboard
    )
