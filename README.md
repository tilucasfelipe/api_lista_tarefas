# api_lista_tarefas 
## Api criada para simular um gerenciador de tarefas que devem ser executadas.

#### O código contém os seguintes módulos:
- flask » Flask, request, jsonify
- json

- (*) As tarefas foram inseridas via código.

#### Siga os passos para realizar os testes:
- Execute o arquivo lista_tarefas.py
- Utilize localhost:5000 como caminho padrão.


#### Metodos:
#### GET:
- /task_by_id/"id_tarefa", onde "id_tarefa" é o id da tafera a ser retornado. Retorna as informações da tarefa com base no ID inserido.
- ex. localhost:5000/task_by_id/1

- /all_tasks. Retorna todas as tarefas existentes.
- ex. localhost:5000/all_tasks

#### POST
- /add_task. Adiciona uma nova tarefa com as informações enviadas. Utiliza-se apenas "responsavel", "tarefa" e "status", pois o "id" é inserido dinamicamente.
- ex. localhost:5000/add_task
- body. {
        'responsavel':'Joao',
        'tarefa':'Reiniciar servidor de impressão',
        'status':'Não inciado'
        }
 

#### PUT
- /alter_task/"id_tarefa", onde "id_tarefa" é o id da tarefa que será alterado. Apenas o status da tarefa pode ser alterado, sendo necessário enviar a requisição com apenas "concluido", "em processo", "iniciado", etc.
- ex. localhost:5000/alter_task/1
- body. {"status":"Concluido"}

#### DELETE
- /alter_task/"id_tarefa", onde "id_tarefa" é o id da tarefa que será excluido.
- - ex. localhost:5000/alter_task/1
