from aiogram import Bot, Dispatcher
import asyncio
token = '6841654844:AAGSv106XBkftoXUKbj-A8-3u1g_kDTEA50'

#создаём объект класса bot, и передаём ему токен
#bot = Bot(token=token)

#объект класса диспетчер - занимается получением апдейтов
#dp = Dispatcher()

#что бы запустить получениие апдейтов, запускаем пуллинг
#dp.start_polling()

#Аиограм библиотека асинхронная, и запускать пуллинг тоже надо асинхронно
#выносим запуск пуллинга в асинхронную функцию

async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

#асинхронно запускаем функцию старт

if __name__ == "__main__":
    asyncio.run(start())
