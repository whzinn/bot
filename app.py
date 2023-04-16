import telebot
def getDigits(text):
    frase = text
    num = ""
    for x in frase:
        if x.isdigit() == True:
            num+=x
    return num

# Token do seu bot (você pode obtê-lo com o BotFather)
TOKEN = '6137176290:AAGQFCsCJpGf3L6MHz5KdmzTkQFBX8UWBFI'

# Cria o objeto bot
bot = telebot.TeleBot(TOKEN)

# Trata o comando '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou o seu bot Telegram.")

@bot.message_handler(commands=['cpf'])
def cpf(message):
    cpf = message.text
    cpf = getDigits(cpf)
    if message.text == "/cpf":
        bot.reply_to(message,"Apos o termo /cpf especifique qual cpf deve ser consultado com 11 digitos 00000000272")
    elif len(cpf) != 11:
        bot.reply_to(message,"Um número CPF contém 11 digitos/caracteres")
    else:
        bot.reply_to(message,"11")
# Trata mensagens normais
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Inicia o bot
bot.infinity_polling()
