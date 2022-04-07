from flask import Flask, request

from main import insertUsuario

app = Flask(__name__)

@app.route("/olamundo", methods = ["GET"])
def olamundo():
    return "Olá Mundo!"

@app.route("/cadastra/usuario", methods = ["POST"])
def cadastraUsuario():

    body = request.get_json()

    if ("nome" not in body):
        return geraResponse(400, "O nome é obrigatório!")
        
    if ("email" not in body):
        return geraResponse(400, "O email é obrigatório!")    

    if ("senha" not in body):
        return geraResponse(400, "A senha é obrigatória!")

    usuario1 = insertUsuario(body["nome"], body["email"], body["senha"])

    return geraResponse(200, "Usuário criado com Sucesso!", "user", usuario1 )

def geraResponse(status, mensagem, nome_do_conteudo = False, conteudo = False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if (nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response    


app.run()

