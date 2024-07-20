import pymongo

uri = "mongodb+srv://hestjs:ki7840800gm@cluster0.ow5effk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)
db = client["meusite"]
usuários = db["usuários"]

async def inserir_usuario(nome, email, senha):
  usuário = {
    "nome": nome,
    "email": email,
    "senha": senha
  }
  usuários.insert_one(usuário)

async def buscar_usuario(email):
  filtro = {"email": email}
  resultado = usuários.find(filtro)
  objeto = {
    "nome": resultado.__getitem__(0)["nome"],
    "email": resultado.__getitem__(0)["email"],
    "senha": resultado.__getitem__(0)["senha"]
  }
  return objeto

async def atualizar_usuario(nome, usuário):
  filtro = {"nome": nome}
  alteração = {
    "$set": {
      "nome": usuário["nome"],
      "email": usuário["email"],
      "senha": usuário["senha"]
    }
  }
  usuários.update_one(filtro, alteração)


async def deletar_usuario(nome):
  filtro = {"nome": nome}
  usuários.delete_one(filtro)