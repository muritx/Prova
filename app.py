import os
from flask import Flask, request

app = Flask(__name__)
aparelhos = [
    {
        "id": 0,
        "marca": "hyperx",
        "nome": "Temp v2"
    },
    {
        "id": 1,
        "marca": "logitech",
        "nome": "G922"
    },
    {
        "id": 5444,
        "marca": "Razer",
        "nome": "Basilisk"
    }
]

@app.route("/", methods=['GET'])
def aparelhos_get():
    return aparelhos

@app.route("/post", methods=['POST'])
def aparelhos_creat():
    novo_aparelho = request.json
    aparelhos.append(novo_aparelho)
    return aparelhos

@app.route("/delete", methods=['DELETE'])
def aparelhos_delet():
    delet_aparelho = request.json
    if delet_aparelho in aparelhos:
        aparelhos.remove(delet_aparelho)
        return aparelhos
    else:
        return "<h1>Aparelho não encontrado!</h1>"
    
@app.route("/put", methods=['PUT'])
def aparelho_put():
    put_aparelho = request.json
    id = put_aparelho.get("id")
    nome = put_aparelho.get("nome")

    
    aparelhos[id]["nome"] = nome
        
    return aparelhos 
 
@app.route("/patch", methods=['PATCH'])
def aparelho_patch():
    patch_aparelho = request.json
    id = patch_aparelho.get("id")
    nome = patch_aparelho.get("nome")
    marca = patch_aparelho.get("marca")
    
    aparelhos[id]["nome"] = nome
    aparelhos[id]["marca"] = marca
        
    return aparelhos  

app.run()

 