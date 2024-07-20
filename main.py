from flask import Flask, jsonify, send_from_directory, request
import asyncio
from database import *

app = Flask(__name__)

@app.route("/")
def homepage():
  return send_from_directory("static", "index.html")
  
@app.route("/criar", methods=["POST"])
def criar():
  async def funcao_criar():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")  
    await inserir_usuario(nome, email, senha)
    return "Usuário criado com sucesso!"
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  result = loop.run_until_complete(funcao_criar())
  return result
  

@app.route("/auth", methods = ["POST"])
def buscar():
  async def funcao_buscar():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")
    try:
      usuário = await buscar_usuario(email)
      if usuário["senha"] == senha:
        return jsonify({
          "auth": True,
          "user": usuário
        })
      else:
        return jsonify({
          "auth": False
        })
    except:
      return jsonify({
        "auth": False
      })
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  result = loop.run_until_complete(funcao_buscar())
  return result


@app.route("/atualizar", methods = ["POST"])
def atualizar():
  async def funcao_atualizar():
    data = request.get_json()
    nome = data.get("nome")
    usuário = data.get("user")
    await atualizar_usuario(nome, usuário)
    return "Usuário atualizado com sucesso!"
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  result = loop.run_until_complete(funcao_atualizar())
  return result

@app.route("/excluir", methods = ["DELETE"])
def excluir():
  async def funcao_excluir():
    data = request.get_json()
    nome = data.get("nome")
    await deletar_usuario(nome)
    return "Usuário excluído com sucesso!"
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  result = loop.run_until_complete(funcao_excluir())
  return result
  
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)

  