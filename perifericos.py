from flask import Flask, request
from bd import aparelhos

api_peri = Flask(__name__)

@api_peri.route("/", methods=['GET'])
def aparelhos_get():
    return aparelhos

@api_peri.route("/post", methods=['POST'])
def aparelhos_creat():
    novo_aparelho = request.json
    aparelhos.append(novo_aparelho)
    return aparelhos

@api_peri.route("/delete", methods=['DELETE'])
def aparelhos_delet():
    delet_aparelho = request.json
    if delet_aparelho in aparelhos:
        aparelhos.remove(delet_aparelho)
        return aparelhos
    else:
        return "<h1>Aparelho não encontrado!</h1>"
    
@api_peri.route("/put", methods=['PUT'])
def aparelho_put():
    put_aparelho = request.json
    id = put_aparelho.get("id")
    nome = put_aparelho.get("nome")

    
    aparelhos[id]["nome"] = nome
        
    return aparelhos 
 
@api_peri.route("/patch", methods=['PATCH'])
def aparelho_patch():
    patch_aparelho = request.json
    id = patch_aparelho.get("id")
    nome = patch_aparelho.get("nome")
    marca = patch_aparelho.get("marca")
    
    aparelhos[id]["nome"] = nome
    aparelhos[id]["marca"] = marca
        
    return aparelhos  
api_peri.run()