
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


keyboard = InlineKeyboardMarkup(row_width=1)

btnenter=InlineKeyboardButton(text="Ввести свои данные", callback_data="enter")
btnprint=InlineKeyboardButton(text="Распечатать свои данные", callback_data="print")

keyboard.insert(btnenter)
keyboard.insert(btnprint)

# entkeyboard = InlineKeyboardMarkup(row_width=1)
# btnname = InlineKeyboardButton(text="Введите свое имя", callback_data="entername")
# btntel = InlineKeyboardButton(text="Отправить свой контакт ☎️",request_contact=True,callback_data="entertel")
# btnfam =  InlineKeyboardButton(text="Введите свою фамилию", callback_data="enterfam")



# entkeyboard.insert(btnname)
# entkeyboard.insert(btnfam)
# entkeyboard.insert(btntel)


#enterKB=InlineKeyboardMarkup(row_width=1)
#enterKB=InlineKeyboardButton(text='Ввести свои данные', callback_data="enter")
