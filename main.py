from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message, ContentType
from aiogram.filters import Command, CommandStart
from aiogram import F
import json
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '6841654844:AAGSv106XBkftoXUKbj-A8-3u1g_kDTEA50'

#создаём объект класса bot, и передаём ему токен
#bot = Bot(token=token)

#объект класса диспетчер - занимается получением апдейтов
#dp = Dispatcher()

#что бы запустить получениие апдейтов, запускаем пуллинг
#dp.start_polling()

#Аиограм библиотека асинхронная, и запускать пуллинг тоже надо асинхронно
#выносим запуск пуллинга в асинхронную функцию

#Функция обработки нажатия кнопки старт

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Mac air13 m1 2020',
            callback_data='apple_air_13_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text= 'Mac pro14',
            callback_data='apple_pro_14_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Apple MacBok pro',
            callback_data='apple_pro_16_u7_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text = 'Link',
            url= 'https://ya.ru'
        )
    ]
])



reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    #Первый ряд
    [
        KeyboardButton(
            text='Ряд 1. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 3. Кнопка 3'
        )
    ],
    #Второй ряд
    [
        KeyboardButton(
            text='Ряд 2. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2 . Кнопка 2'
        )
    ],
    #Третий ряд
    [
        KeyboardButton(
            text='Ряд 3. Кнопка 1'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Подсказка', selective=True)

#отдельная клавиатура, для викторины и геолокации
loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='geo',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='kont',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Victorina',
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='подсказка')

#Будем показвать эту клавиатуру при нажатии кнопки старт


#функция для инлайн клавиатуры
async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}. Показываю инлайн клавиатуру')

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Кнопка 1')
    keyboard_builder.button(text='Кнопка 2')
    keyboard_builder.button(text='Кнопка 3')
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='подсказка')

async def start_bot(bot: Bot):
    await get_command(bot)
    await bot.send_message(446159753, text='Бот запущен')
async def stop_bot(bot: Bot):
    await bot.send_message(446159753, text='Бот остановлен')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отправлена фотография')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_location(message: Message, bot: Bot):
    await message.answer(f'Отправлена геолокация\r\a'
                         f'{message.location.latitude} \r\n {message.location.longitude}')

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name} 1', reply_markup=get_reply_keyboard())


async def get_hello(message: Message, bot: Bot):
    await message.answer('def get_hello')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)

async def get_command(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description= 'Старт (get_command)'
        ),
        BotCommand(
            command='help',
            description='Помощь (get_command)'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_location, F.location, F.text == '@aiogram_trainig_bot geo')
    #dp.message.register(get_start, CommandStart)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == '@aiogram_trainig_bot Привет')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

#асинхронно запускаем функцию старт

if __name__ == "__main__":
    asyncio.run(start())
