from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import sqlite3

bot = AsyncTeleBot('6000559993:AAFl7pLjyLw6tWeSa31-OZ0_muDyPAE9INQ')
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print('1')
#make dictionary
@bot.message_handler(commands=['start'])
async def st(message):
    await bot.send_message(message.chat.id, 'Введите')
@bot.message_handler(commands=['help'])
async def start_message(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('\U0001F4B0 Инвестиционный портфель')
    btn2 = KeyboardButton('\U0001f3e6 Денежные операции')
    btn3 = KeyboardButton('Чат с менеджером')
    btn4 = KeyboardButton('Помощь')
    markup.add(btn1, btn2, btn3, btn4)
    await bot.send_message(message.chat.id, 'Привет!\n'
                                            'Вы находитесь в главном меню!', reply_markup=markup)

@bot.message_handler(func= lambda message: message.text in ['\U0001F4B0 Инвестиционный портфель',
                                                            '\U0001f3e6 Денежные операции',
                                                            'Чат с менеджером',
                                                            'Помощь',
                                                            '\u2B05 Главное меню'])
async def head_menu(message):
    if (message.text == '\U0001F4B0 Инвестиционный портфель'):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = KeyboardButton('\U0001F4B1 Договор')
        btn2 = KeyboardButton('\u2B05 Главное меню')
        markup.add(btn1, btn2)
        name = 'Иванов'
        cursor.execute("SELECT all_money FROM main WHERE Last_name = ?", (name,))
        results = cursor.fetchall()
        await bot.send_message(message.chat.id, results[0][0], reply_markup=markup)
    elif (message.text == '\U0001f3e6 Денежные операции'):
        markup_one = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('Пополнить')
        btn2 = KeyboardButton('Вывод')
        btn3 = KeyboardButton('\u2B05 Главное меню')
        markup_one.add(btn1, btn2, btn3)
        await bot.send_message(message.chat.id, 'тут выбрать что хотим',
                               reply_markup=markup_one)
    elif (message.text == 'Чат с менеджером'):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('Продление договора')
        btn2 = KeyboardButton('Вопрос')
        btn3 = KeyboardButton('\u2B05 Главное меню')
        markup.add(btn1, btn2, btn3)
        await bot.send_message(message.chat.id, 'выбрать действие', reply_markup=markup)
    elif (message.text == 'Помощь'):
        await bot.send_message(message.chat.id, 'справочная информация')
    elif (message.text == '\u2B05 Главное меню'):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('\U0001F4B0 Инвестиционный портфель')
        btn2 = KeyboardButton('\U0001f3e6 Денежные операции')
        btn3 = KeyboardButton('Чат с менеджером')
        btn4 = KeyboardButton('Помощь')
        markup.add(btn1, btn2, btn3, btn4)
        await bot.send_message(message.chat.id, 'вернулись в меню', reply_markup=markup)

@bot.message_handler(func= lambda message: message.text in ['\U0001F4B1 Договор'])
async def invest_protfel(message):
    if (message.text == '\U0001F4B1 Договор'):
        await bot.send_message(message.chat.id, 'тут выводится pdf файл с договором')

@bot.message_handler(func= lambda message: message.text in ['Пополнить', 'Вывод'])
async def money_flow(message):
    if (message.text == 'Пополнить'):
        await bot.send_message(message.chat.id, 'выводится реквизит счета и фунцкия добавления фото чека')
    elif (message.text == 'Вывод'):
        await bot.send_message(message.chat.id, 'Указывается сумма и дата вывода')

@bot.message_handler(func=lambda message: message.text in ['Продление договора', 'Онлайн', 'Встреча', 'Вопрос', 'back'])
async def chat_with_manager(message):
    if (message.text == 'Продление договора'):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = KeyboardButton('Онлайн')
        btn2 = KeyboardButton('Встреча')
        btn3 = KeyboardButton('back')
        markup.add(btn1, btn2, btn3)
        await bot.send_message(message.chat.id, 'выберите', reply_markup=markup)
    elif (message.text == 'Онлайн'):
        await bot.send_message(message.chat.id, 'выбрали онлайн')
    elif (message.text == 'Встреча'):
        await bot.send_message(message.chat.id, 'выбрали оффлайн')
    elif (message.text == 'Вопрос'):
        await bot.send_message(message.chat.id, 'Введите свой вопрос')
    elif (message.text == 'back'):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('Продление договора')
        btn2 = KeyboardButton('Вопрос')
        btn3 = KeyboardButton('\u2B05 Главное меню')
        markup.add(btn1, btn2, btn3)
        await bot.send_message(message.chat.id, 'выбрать действие', reply_markup=markup)

@bot.message_handler(func= lambda message: True)
async def save_input(message):
    user_input = message.text
    print(user_input)
    await bot.send_message(message.chat.id, 'Вы ввели ' + user_input)



if __name__ == '__main__':
    asyncio.run(bot.polling())
