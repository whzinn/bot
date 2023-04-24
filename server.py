
from requests import get

def getData(data, separador):
	data = data.split(separador)[1]
	cont = 0
	for c in data:
		if c == '"':
			return data[0:cont]
		else:
			cont += 1

def hello(cpf):
    if len(cpf) != 11 or cpf.isdigit() == False:
        return {
            "status":900,
            "noticia":"CPF INVALIDO"
        }
    data = get(f"http://pat.mte.gov.br/sistemas/pnpeweb/pnpepesquisas.asp?acao=consultar%20cpf&cpf={cpf}").text
    if '<ROOT/>' in data:
        return {
            "status":400,
            "noticia":"CPF INVALIDO ou NAO FOI ENCONTRADO"
        }
    allData = {
        "status":200,
        "noticia":"Seu CPF foi consultado",
        "cpfConsultado":getData(data, 'NRCPF="'),
        "nomeCompleto":getData(data, 'NOPESSOAFISICA="'),
        "dataNascimento":getData(data, 'DTNASCIMENTO="'),
        "nomeDaMae":getData(data, 'NOMAE="'),
        "nomeLogradouro":getData(data, 'NOLOGRADOURO="'),
        "numeroLogradouro":getData(data, 'NRLOGRADOURO="'),
        "dsComplemento":getData(data, 'DSCOMPLEMENTO="'),
        "nomeBairro":getData(data, 'NOBAIRRO="'),
        "nomeMunicipio":getData(data, 'NOMUNICIPIO="'),
        "SiglaEstadoBrasileiro":getData(data, 'SGUF="'),
        "cep":getData(data, 'NRCEP="')}
    print(allData)
    return allData
