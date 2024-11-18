from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
  { "label": "Mi primera tarea", "done": False },
  { "label": "Mi segunda tarea", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
        return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
     if position >= len(todos):
          return jsonify({
               "message": "La tarea no existe."
          }), 404
     todos.pop(position)
     return jsonify(todos), 200     


# Estas líneas SIEMPRE van al final
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)