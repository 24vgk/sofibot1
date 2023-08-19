from aiogram import Router, types, Bot
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Text

from keyboards.inline.keyboard import create_inline_kb
from lexicon.lexicon import LEXICON_RU, LEXICON_COMMANDS_RU, LEXICON_COMMANDS_RU_TEST, LEXICON_SRC_HI_RU_TEST, LEXICON_COMMANDS_RU_UPR, LEXICON_SRC_HI_RU_UPR


# Инициализируем роутер уровня модуля
router: Router = Router()
keyboard = create_inline_kb(2, **LEXICON_COMMANDS_RU)
keyboard_test = create_inline_kb(2, last_btn='ПЕРЕЙТИ В КАНАЛ', last_btn1='Назад', **LEXICON_COMMANDS_RU_TEST)
keyboard_upr = create_inline_kb(2, last_btn='ПЕРЕЙТИ В КАНАЛ', last_btn1='Назад', **LEXICON_COMMANDS_RU_UPR)
file = FSInputFile('1.jpg')

global m


async def glob(bot: Bot):
    await bot.delete_message(message_id=m.message_id, chat_id=m.chat.id)


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    global m
    m = await message.answer_photo(photo=file, caption=LEXICON_RU['/start'], reply_markup=keyboard)


# Обработчик нажатия на кнопку Назад
@router.callback_query(Text(text=['last_btn1']))
async def buttons_press_info(callback: CallbackQuery, bot: Bot):
    try:
        await glob(bot)
    except Exception:
        pass
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_RU['/start']),
            reply_markup=keyboard
        )
    except Exception:
        global m
        m = await m.answer_photo(photo=file, caption=LEXICON_RU['/start'], reply_markup=keyboard)


# Обработчик нажатия на кнопку Упражнения
@router.callback_query(Text(text=['/1']))
async def buttons_press_info(callback: CallbackQuery, bot: Bot):
    try:
        await glob(bot)
    except Exception:
        pass
    global m
    try:
        m = await m.answer(
            text='<b>5 дыхательных упражнений, чтобы справиться с тревогой</b>👇🏽',
            reply_markup=keyboard_upr
        )
    except Exception:
        m = await m.answer(
            text='<b>5 дыхательных упражнений, чтобы справиться с тревогой</b>👇🏽',
            reply_markup=keyboard_upr
        )


# Обработчик нажатия на кнопку Тесты
@router.callback_query(Text(text=['/2']))
async def buttons_press_rules(callback: CallbackQuery, bot: Bot):
    try:
        await glob(bot)
    except Exception:
        pass
    global m
    try:
        m = await m.answer(
            text='<b>Тесты помогают нам лучше понять себя, а также шагнуть в сторону изменений и роста</b>⬇️☺️',
            reply_markup=keyboard_test
        )
    except Exception:
        m = await m.answer(
            text='<b>Тесты помогают нам лучше понять себя, а также шагнуть в сторону изменений и роста</b>⬇️☺️',
            reply_markup=keyboard_test
        )



# Обработчик нажатия на кнопку ПЕРЕЙТИ В КАНАЛ
@router.callback_query(Text(text=['/3', '/5t', 'last_btn']))
async def buttons_press_support(callback: CallbackQuery):
    await callback.answer(url='https://t.me/+KnJIIJd_tlhiMDBi')


# Обработчик нажатия на кнопку Тест 1
@router.callback_query(Text(text=['/1t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_TEST['/1t']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/1t'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Тест 2
@router.callback_query(Text(text=['/2t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_TEST['/2t']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/2t'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Тест 3
@router.callback_query(Text(text=['/3t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_TEST['/3t']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/3t'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Тест 4
@router.callback_query(Text(text=['/4t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_TEST['/4t']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/4t'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Упражнение 1
@router.callback_query(Text(text=['/1u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_UPR['/1u']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_UPR['/1u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Упражнение 2
@router.callback_query(Text(text=['/2u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_UPR['/2u']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_UPR['/2u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Упражнение 3
@router.callback_query(Text(text=['/3u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_UPR['/3u']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_UPR['/3u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Упражнение 4
@router.callback_query(Text(text=['/4u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_UPR['/4u']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_UPR['/4u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Упражнение 5
@router.callback_query(Text(text=['/5u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_SRC_HI_RU_UPR['/5u']),
            reply_markup=callback.message.reply_markup
        )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_UPR['/5u'],
            reply_markup=callback.message.reply_markup
        )