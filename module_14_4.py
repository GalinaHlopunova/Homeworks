import keyboard
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import get_all_products

import crud_functions

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button1)
kb.add(button2)
kb.add(button3)

kb2 = InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text="Product1", callback_data='product_buying')
button5 = InlineKeyboardButton(text="Product2", callback_data='product_buying')
button6 = InlineKeyboardButton(text="Product3", callback_data='product_buying')
button7 = InlineKeyboardButton(text="Product4", callback_data='product_buying')
kb2.add(button4)
kb2.add(button5)
kb2.add(button6)
kb2.add(button7)

products = get_all_products()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Start message")
    await message.answer("Я могу рассчитать суточную норму калорий для женщин - нажмите 'Рассчитать'. "
                         "Для получения информации - нажмите 'Информация'. "
                         "Также я могу предложить купить полезные продукты - для этого нажмите 'Купить'.",
                         reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    n = 0
    for product in products:
        n += 1
        await message.answer(f"Название: {product[1]} | Описание: {product[2]}"
                             f"| Цена: {product[3]}")
        with open(f"files/{n}.jpg", 'rb') as img:
            await message.answer_photo(img, reply_markup=kb)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text='Информация')
async def get_formulas(message: types.Message):
    await message.answer("10хвес(кг)+6,25хрост(см)-5хвозраст(г)-161")


@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст (полных лет):")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес (в кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    NK = 10 * int(data['third']) + 6.25 * int(data['second']) - 5 * int(data['first']) - 161
    await message.answer(f"Ваша норма калорий {NK}")
    await state.finish()


@dp.message_handler()
async def all_massages(message: types.Message):
    print("Привет!")
    await message.answer("Привет! Я бот, помогающий твоему здоровью. "
                         "Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)