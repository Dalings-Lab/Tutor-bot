import asyncio

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils import executor

from read_questions import text_of_bilet

try:
    bot = Bot(token='***', parse_mode="HTML")
    dp = Dispatcher(bot)

    numero_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    numero_markup.row("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    numero_markup.row("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    numero_markup.row("Тест")

    otvet_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    otvet_markup.row("Показать ответ")
    otvet_markup.row("Назад")

    @dp.message_handler(commands=['start'])
    async def start(message):
        await message.answer("Добро пожаловать", reply_markup=numero_markup)

        await asyncio.sleep(600)
        await message.delete()
        await bot.delete_message(message.chat.id, message.message_id + 1)


    @dp.message_handler(regexp="Тест")
    async def test(message):
        await message.answer("Это тест")
        await message.delete()

    @dp.message_handler(regexp="1")
    @dp.message_handler(regexp="2")
    @dp.message_handler(regexp="3")
    @dp.message_handler(regexp="4")
    @dp.message_handler(regexp="5")
    @dp.message_handler(regexp="6")
    @dp.message_handler(regexp="7")
    @dp.message_handler(regexp="8")
    @dp.message_handler(regexp="9")
    @dp.message_handler(regexp="10")
    @dp.message_handler(regexp="11")
    @dp.message_handler(regexp="12")
    @dp.message_handler(regexp="13")
    @dp.message_handler(regexp="14")
    @dp.message_handler(regexp="15")
    @dp.message_handler(regexp="16")
    @dp.message_handler(regexp="17")
    @dp.message_handler(regexp="18")
    @dp.message_handler(regexp="19")
    @dp.message_handler(regexp="20")
    async def choose_bilet(message):
        msg_text = int(message.text)
        photo = open('photo/' + str(msg_text) + '.png', 'rb')

        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=text_of_bilet(msg_text),
                             reply_markup=otvet_markup)

        await message.delete()
        await asyncio.sleep(600)
        await bot.delete_message(message.chat.id, message.message_id + 1)


    @dp.message_handler(regexp="Показать ответ")
    async def otvet(message):
        await message.answer('Ответ', reply_markup=numero_markup)

        await message.delete()
        await asyncio.sleep(600)
        await bot.delete_message(message.chat.id, message.message_id + 1)


    @dp.message_handler(regexp="Назад")
    async def otvet(message):
        await message.answer('Выберите вопрос', reply_markup=numero_markup)

        await message.delete()
        await asyncio.sleep(600)
        await bot.delete_message(message.chat.id, message.message_id + 1)

    if __name__ == '__main__':
        executor.start_polling(dp)

except:
    pass
