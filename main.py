import logging
from aiogram import Bot, types
from aiogram.types.message import  ContentType
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.utils.markdown import text, bold, italic 
from aiogram.types import ParseMode, user
from aiogram.types import CallbackQuery
from features.steps.config import MY_ID, TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



import logging

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
#dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO)

# Для машины состояний (ввода информации)
class user():
  name_user = ""
  fname_user = ""
  tel_user = ""

# Для машины состояний 
class reg(StatesGroup):
    name =  State()
    fname = State()
    tel = State()

# запуск бота командой старт
@dp.message_handler(commands=['start'],state = "*")
async def process_start_command(message: types.Message):
        await message.answer(text="Добро пожаловать в МиниБот!", reply_markup=keyboard)
        await bot.send_message(MY_ID, "start+1")

# нажатие первой кнопки
@dp.callback_query_handler(text_contains="enter", state="*")
async def process_enter_command(call:CallbackQuery,state: FSMContext):
         await call.bot.send_message(call.from_user.id,'⭐ Введите ваши данные ⭐')
         await call.message.answer(text='💬 Введите ваше имя 💬')
         await reg.name.set()
         
         
# начало работы машины состояний
@dp.message_handler(state=reg.name, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    if any(map(str.isdigit, message.text)):
        await message.reply("✋ Вы ошиблись, попробуйте ввести имя снова ✋")
        return
    await state.update_data(name_user=message.text.title())
    user.name_user = message.text
    await message.answer(text='💬 Введите вашу фамилию 💬')
    await reg.fname.set()
    


@dp.message_handler(state=reg.fname, content_types=types.ContentTypes.TEXT)
async def age_step(message: types.Message, state: FSMContext):
    if any(map(str.isdigit, message.text)):
        await message.reply("✋ Вы ошиблись, попробуйте ввести фамилию снова ✋")
        return
    await message.answer(text="☎️ Введите свой телефон ☎️            (без +)")
    await state.update_data(fname_user=message.text.title())
    user.fname_user=message.text
    await reg.tel.set()
    await user.tel_user.set()


@dp.message_handler(state=reg.tel, content_types=types.ContentTypes.TEXT)
async def res_step(message: types.Message, state: FSMContext):
    if not any(map(str.isdigit, message.text)):
        await message.reply(text="✋ Вы ошиблись, попробуйте ввести свой телефон снова ✋")
        return
    await state.update_data(tel_user=message.text.lower())
    user_data = await state.get_data()
    user.tel_user = message.text
    await state.finish()
    await message.answer(text="⭐ Вы успешно занесли свои данные ⭐")
        

# нажатие второй кнопки
@dp.callback_query_handler(text_contains="print")
async def process_print_command(call:CallbackQuery,state: FSMContext):
         await call.bot.send_message(call.from_user.id,'⭐ Распечатка ваших данных               /print⭐')
        
# запуск печати
@dp.message_handler(commands = ["print"], )
async def printer(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text(
                text('Добро пожаловать,', user.name_user),
                text('Тел:', user.tel_user),
                sep='\n',
            ))

# команды бота
@dp.message_handler(commands=['help'], state="*")
async def process_help_command(message: types.Message):
    await message.reply("Список имеющихся команд: \n/start - начало программы, позволяет вам увидеть функционал бота\n/print - распечатывает данные\n/help - помощь\n")

# обработка не тех сообщений
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(('Я не знаю, что с этим делать :('),
                        italic('\nВведите команду /help'), )
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)

# конец
async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp,on_shutdown=shutdown)


