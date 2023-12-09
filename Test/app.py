from flask import Flask, make_response, jsonify, request
from BancoDeDados import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


#BUSCA CARROS
@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(dados = Carros ))

#BUSCA CARROS POR ID 
@app.route('/carros/<int:id>', methods=["GET"])
def get_carros_by_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)
        else:
            return print('Erro')
        
#ADICIONAR CARROS NA LISTA
@app.route('/carros',methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return carro

# ATUALIZA CARROS NA LISTA POR ID
@app.route('/carros/<int:id>', methods=["PUT"])
def update_carro(id):
    carro_update = request.get_json()
    for indice,carro in enumerate (Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_update)
            return jsonify(Carros[indice])

#DELETA CARROS POR ID 
@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    for indice,carro_delete in enumerate (Carros):
        if carro_delete.get('id') == id:
            del Carros[indice]
            return jsonify(massage="success")
    return Carros


app.run()