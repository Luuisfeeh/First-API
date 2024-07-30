# O que é uma API?? é um lugar para disponibilizar recursos e/ou funcionalidades

# Objetivo da API - Criar uma api para disponibilizar a consulta , criação , edição e exclusão de livros
# URL Base - localhost (gratuito)
# EndPoints: 
#   - localhost/livros (GET) "Consultar o livro"
#   - localhost/livros (POST) "Criar novos livros"
#   - localhost/livros/id (GET) "Buscar o livro pelo id ou especifico"
#   - localhost/livros/id (PUT) "Poder modificar o livro"
#   - localhost/livros/id (DELETE) "Poder deletar o livro"
# Quais recursos - LIVROS

from flask import Flask, jsonify , request

FistAPI = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Fantasma da Ópera',
        'autor': 'Gaston Leroux'
    },
    {
        'id': 2,
        'título': 'Noiva',
        'autor': 'Ali Hazelwwod',
    },
    {
        'id': 3,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    }
]


# Consultar (TODOS)
@FistAPI.route('/livros',methods = ['GET'])
def consultar_livros():
    return jsonify(livros)

# Consultar (ID)
@FistAPI.route('/livros/<int:id>', methods =['GET'])
def consultar_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Editar
@FistAPI.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
@FistAPI.route('/livros', methods =['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# Excluir
@FistAPI.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


# Iniciar a API 

FistAPI.run(port=5000,host='localhost',debug=True)
