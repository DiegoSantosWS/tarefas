from flask import Flask, jsonify


app = Flask('todoapp')
tarefas = [{'id': 1, 'titulo':'titulo', 'descricao':'descricao', 'estado':False}]


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)

