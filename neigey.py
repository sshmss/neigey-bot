import telebot

bot = telebot.TeleBot(open('.key').read(), parse_mode='html')

@bot.message_handler(commands=['start'])
def timetable_handler(message):
    bot.reply_to(message, 'pls divehin liyaccey i laduganay')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    neigey_message = message.text
    neigey_endings = {"o": "w", "aa": "r"}
    neigey_letters = {"dh": "d", "oo": 'u', "th": "t", "ey": "ay", "ch": "cc", "ai": "a", "aa": "w"}

    neigey_splits = neigey_message.split(" ")
    neigay_message = []
    for word in neigey_splits:
        for (key, value) in neigey_endings.items():
            if word[-1] == key:
                word = word[:-1]
                word = word + value
        neigay_message.append(word)
    
    neigey_message = ' '.join(neigay_message)
        
    for (key, value) in neigey_letters.items():
        # print(key, value)
        if key in neigey_message:
            neigey_message = neigey_message.replace(key, value)

    # neigey_message = neigey_message + str(message)
    
    bot.reply_to(message, neigey_message)

bot.polling()