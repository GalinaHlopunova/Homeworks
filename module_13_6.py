import keyboard
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button2 = InlineKeyboardButton(text="Формулы расчета", callback_data='formulas')
kb.add(button)
kb.add(button2)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Start message")
    await message.answer("Я могу рассчитать суточную норму калорий для женщин. "
                         "Введите 'Рассчитать'")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10хвес(кг)+6,25хрост(см)-5хвозраст(г)-161")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст (полных лет):")
    await UserState.age.set()
    await call.answer()


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
