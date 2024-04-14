from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message, ContentType
from aiogram.filters import Command, CommandStart
from aiogram import F
import json
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

async def start_bot(bot: Bot):
    await bot.send_message(446159753, text='Бот запущен')
async def stop_bot(bot: Bot):
    await bot.send_message(446159753, text='Бот остановлен')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отправлена фотография')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')



async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name} 1')
    await message.answer(f'Hello {message.from_user.first_name} 2')
    await message.reply(f'Hello {message.from_user.first_name} 3')

async def get_hello(message: Message, bot: Bot):
    await message.answer('def get_hello')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=['start', 'run']))
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
