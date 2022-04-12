# Importando os pacotes necessários para utilizar o REST
from flask import Flask, request, jsonify
import json

# Criação de ALIAS "app" para utilizar os metodos FLASK
app = Flask(__name__)

# Lista de tarefas estática para teste dos verbos
lista_tarefa = [
    {
        'id':'0',
        'responsavel':'Lucas',
        'tarefa':'MicroService - consulta',
        'status':'Em processo'
    },

    {
        'id':'1',
        'responsavel':'Lucas',
        'tarefa':'MicroService - altera',
        'status':'Em processo'
    },

    {
        'id': '2',
        'responsavel': 'Lucas',
        'tarefa': 'MicroService - exclui',
        'status': 'Em processo'
    },

   {
       'id': '3',
       'responsavel': 'Lucas',
       'tarefa': 'MicroService - inclui',
       'status': 'Em processo'
   }
]

# Criação da rota inicial "/"
@app.route('/')
def pagina_inicial():
    return ("A API ESTÁ DE PÉ!")

# Get que retorna as tarefas por ID. Ex. "/task_by_id/1". Este caso é apenas GET
@app.route('/task_by_id/<int:id>', methods = ['GET'])
def task_by_id(id):
    try:
        if request.method == 'GET':
            response = lista_tarefa[id]
            return jsonify(response)
    except IndexError:
        return (f'Não foi possível identificar o índice {id}! Verifique ou contate o administrador do sistema!')

# Get que retorna todas as tarefas. Ex. "/all_tasks/". Este caso é apenas GET
@app.route('/all_tasks', methods = ['GET'])
def all_task():
    if request.method == 'GET':
        response = lista_tarefa
        return jsonify(response)

# Esta rota permite a alteração ou exclusão de algum item no plano de tarefas, apenas com PUT ou DELETE.
# Para a alteração é enviado um PUT com ID e status da tarefa, pois a alteração não é permitida nos demais.
# Para a exclusão, um DELETE é enviado com o ID da tarefa.
@app.route('/alter_task/<int:id>', methods=['PUT','DELETE'])
def alter_task(id):
# A validação do método é realizada na próxima linha como sendo um PUT
    if request.method == 'PUT':
        try:
            dado = json.loads(request.data)
            (lista_tarefa[id])['status'] = dado['status']
            return (f'Alteração do id {id} realizada com sucesso!')
        except IndexError:
            return (f'Não foi possível identificar o índice {id}! Verifique ou contate o administrador do sistema!')

    elif request.method == 'DELETE':
        try:
            lista_tarefa.pop(id)
            return (f'Registro {id} excluído com sucesso.')
        except IndexError:
            return (f'Não foi possível identificar o índice {id}! Verifique ou contate o administrador do sistema!')

# Esta rota permite a inclusão de algum item no plano de tarefas, apenas o POST é permitido.
# Para a alteração é enviado um POST com os campos responsavel, status e tarefa, pois o id é inserido dinamicamente em
# dados['id'] = posicao.
# Exemplo:
# {
#     "responsavel": "Pedro José",
#     "tarefa": "Criar Serviço de consulta ao microserviço Correios"
#     "status": "Não iniciado",
# }
@app.route('/add_task/', methods = ['POST'])
def adicionar():
    dados = json.loads(request.data)
    posicao = len(lista_tarefa)
    dados['id'] = posicao
    lista_tarefa.append(dados)
    print(lista_tarefa)
    return (f'Dados inseridos: {dados}!')

# Inicializa a API
if __name__ == ("__main__"):
    app.run(debug=True)