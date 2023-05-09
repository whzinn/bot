import telebot, requests, json, re
import server
bot = telebot.TeleBot("1995700005:A")

def cpf(men):
  id1 = men.chat.id
  txt = men.text
  if men.text == "/cpf":
    bot.reply_to(men, "*Você não digitou o cpf em seguida, por favor tente novamente.*", parse_mode="Markdown")
  else:
    try:
      msg = men.text
      ip = re.sub('[^0-9]', '', msg)
      print(ip)
      req = server.hello(ip)
      op = req["dataNascimento"][6:]
      jog = 2023 - int(op)
      response = f'🔍 CONSULTA DE CPF 🔍\n\n*• CPF*: `{req["cpfConsultado"]}`\n*• NOME*: `{req["nomeCompleto"]}`\n*• MÃE*: `{req["nomeDaMae"]}`\n*• NASCIMENTO*: `{req["dataNascimento"]}`\n*• IDADE*: `{jog}`\n\n*• Endereço*\n*• ESTADO*: `{req["nomeMunicipio"]}`\n*• SIGLA ESTADO*: `{req["SiglaEstadoBrasileiro"]}`\n*• BAIRRO*: `{req["nomeBairro"]}`\n*• CEP*: `{req["cep"]}`\n*• LOGRADOURO*: `{req["nomeLogradouro"]}`\n*• NUMERO*: `{req["numeroLogradouro"]}`\n*• COMPLEMENTO*: `{req["dsComplemento"]}`\n\n*• by*: @buscacpfbot'
      bot.reply_to(men, response, parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(men, "cpf informado realmente é invalido ou inexistente.", parse_mode="Markdown")
