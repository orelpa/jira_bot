from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
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





async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name} 1')
    await message.answer(f'Hello {message.from_user.first_name} 2')
    await message.reply(f'Hello {message.from_user.first_name} 3')

async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.message.register(get_start)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

#асинхронно запускаем функцию старт

if __name__ == "__main__":
    asyncio.run(start())
