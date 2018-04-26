import telebot
from telebot import types

TOKEN = '570763381:AAGiEjD2LBj_i8fBLPjf2qDVfaXMZDm1T5o'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Да', 'Нет']])
    msg = bot.send_message(m.chat.id, 'Привет, желаешь внести депозит?'
    ,reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
    if m.text == 'Нет':
        bot.send_message(m.chat.id, 'Жаль, тогда всего хорошего :)')

    elif m.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        itembtna = types.KeyboardButton('0,01 BTC')
        itembtnv = types.KeyboardButton('0,1 BTC')
        itembtnc = types.KeyboardButton('0,25 BTC')
        itembtnd = types.KeyboardButton('0,5 BTC')
        itembtne = types.KeyboardButton('0,75 BTC')
        itembtnp = types.KeyboardButton('1 BTC')
        markup.row(itembtna, itembtnv,itembtnc )
        markup.row(itembtnd, itembtne,itembtnp )
        bot.send_message(m.chat.id, 'Выбери,сколько хочешь внести :',reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def bbb(m):
        bot.send_message(m.chat.id, 'Отлично, переведи свой депозит на этот кошелек:БИТКОИНМИЛЛИОНЕРНИКИТА')
        bot.send_message(m.chat.id, 'Спасибо за использование нашего бота!')

@bot.message_handler(commands=['help'])
def help(m):
   bot.send_message(m.chat.id,'Нужна помощь? Обращайся на почту: btcdepositbot@gmail.com')

bot.polling()
