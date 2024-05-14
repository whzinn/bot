import telebot
from mp import pix
import botcpf
import pyshorteners
def getDigits(text):
    frase = text
    num = ""
    for x in frase:
        if x.isdigit() == True:
            num+=x
    return num

menu = """
[+] BUSCAR CNPJ:` /cnpj 00000000001910` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] CONSULTAR CPF:` /cpf1 00000000272` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] BUSCAR CPF:` /cpf 00000000272` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] BUSCAR CEP: `/cep 01001000` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] GERAR CPF:` /gerarcpf` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] GERAR CNPJ:` /gerarcnpj 10` | vip 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] BUSCAR CELULAR:` /celular 21995854873` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--
[+] BUSCAR NOME COMPLETO:` /nome Jair Bolsonaro` | vip
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
[+] BUSCAR PLACA: ` /placa ABC1234` | vip
"""



# Token do seu bot (você pode obtê-lo com o BotFather)
TOKEN = '5673249759:AAHmH3g_vuY2u1jXFa6YSHOJfxu_RLghtHA'


# Cria o objeto bot
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['cpf'])
def cpf(message):
    cpf = message.text
    cpf = getDigits(cpf)
    if message.text == "/cpf":
        bot.reply_to(message,"Apos o termo /cpf especifique qual cpf deve ser consultado com 11 digitos 00000000272")
    elif len(cpf) != 11:
        bot.reply_to(message,"Um número CPF contém 11 digitos/caracteres")
    else:
        botcpf.cpf(message)
@bot.message_handler(commands=['menu'])
def send_welcome(message):
    bot.reply_to(message, menu, parse_mode='Markdown')
# Trata o comando '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, menu, parse_mode='Markdown')

@bot.message_handler(commands=['comprar'])
def comprar(message):

    caption = "*Acesse o link de pagamento no Valor de 39.99 e pague via pix*"

    photo = open("logo.png","rb")
    bot.send_photo(message.chat.id,photo=photo,caption=caption,parse_mode='Markdown')
    link = "https://pagamento.onrender.com/source.html"
    s = pyshorteners.Shortener()
    link = s.tinyurl.short(link)
    bot.reply_to(message,f"*Link de pagamento*: {link}",parse_mode="Markdown")
    #bot.reply_to(message,f"*Pague com o cartão de credito*: https://n9.cl/kbpio",parse_mode="Markdown")
    bot.reply_to(message,"*duvidas tirar com*: @whzinn",parse_mode='Markdown')
# Trata mensagens normais
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "*• Compre acesso para poder usar este comando. use /comprar para comprar com pix*",parse_mode='Markdown')

# Inicia o bot
bot.infinity_polling()
