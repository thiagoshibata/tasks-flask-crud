from flask import Flask, request, jsonify
from models.task import Task
# manual: __name = "__main__"
app = Flask(__name__)

tasks = []
task_id_control = 1

# -- START ROUTES --

# CREATE
@app.route("/tasks", methods=['POST'])
def create_task():
  global task_id_control # variável global para ser acessada de dentro da função
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message":"Nova tarefa criada com sucesso!", "id": new_task.id})

# READ ALL
@app.route("/tasks", methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]
  output = {
          "tasks": task_list,
          "total_tasks": len(task_list)
        }
  
  return jsonify(output)

# Utilizando parâmetros de rota
# possibilita que receba uma informação do cliente
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())
  
  return jsonify({"message":"Não foi possível encontrar a atividade"}), 404

# UPDATE
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
  print(task)
  if task == None:
    return jsonify({"message":"Não foi possível encontrar a atividade"}), 404
  
  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  print(task)
  return jsonify({"message":"Tarefa atualizada com sucesso"})

# DELETE
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break
  if not task:
    return jsonify({"message":"Não foi possível encontrar a atividade"}), 404
  
  tasks.remove(task)
  return jsonify({"message":"Tarefa deletada com sucesso"})

# -- END ROUTES

if __name__ == "__main__":
  app.run(debug=True)
