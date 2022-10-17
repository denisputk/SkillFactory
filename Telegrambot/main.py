import telebot
from telebot import types
from config import exchanges, TOKEN
from extensions import ApiException, Converter

def create_markup(base = None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in exchanges.keys():
        if val != base:
            buttons.append(types.KeyboardButton(val.capitalize()))

    markup.add(*buttons)
    return markup

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Teid tervitab valuutakalkulaator!\n \
Valuuta loetelu /values \n \
Vajutage linki alustamiseks /convert'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Valuuta loetelu:'
    for key in exchanges.keys():
        text = '\n'.join((text, key, ))
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['convert'])
def values(message: telebot.types.Message):
    text = 'Mida soovite müüja?'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, base_handler)

def base_handler(message: telebot.types.Message):
    base = message.text.strip()
    text = 'Mida soovite osta?'
    bot.send_message(message.chat.id, text, reply_markup=create_markup(base))
    bot.register_next_step_handler(message, quote_handler, base)

def quote_handler(message: telebot.types.Message, base):
    quote = message.text.strip()
    text = 'Sisestage kogus:'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, base, quote)

def amount_handler(message: telebot.types.Message, base, quote):
    amount = message.text.strip()
    try:
        new_price = Converter.get_price(base, quote, amount)
    except ApiException as e:
        bot.send_message(message.chat.id, f'Valuutavahetse viga: \n{e}')
    else:
        text = f'Hind {amount} {base} = {new_price} {quote}'
        bot.send_message(message.chat.id, text)

bot.polling()
