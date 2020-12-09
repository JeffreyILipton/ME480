from flask import Flask, jsonify, request, abort, make_response


app = Flask(__name__)

tasks = []
t1 = {
    'id':1,
    'title': 'Buy groceries',
    'description': 'Soylent Green, Soylent Brown, Soylent Red',
    'done': False
}

t2 = {
    'id':2,
    'title': 'Learn Python',
    'description': 'get matrix port installed and have tank download it',
    'done': False
}
tasks.append(t1)
tasks.append(t2)


@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks":tasks})

@app.route('/todo/tasks/<int:task_id>')
def get_taskByID(task_id):
    taskided = [task for task in tasks if task['id']== task_id]
    if len(taskided)==0:
        abort(404)
    return jsonify({'task' : taskided[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

def makeTask(title,description='',completion=False):
    ids = [task['id'] for task in tasks]
    nid = max(ids)+1
    task = {
        'id':nid,
        'title': title,
        'description': description,
        'done': completion
    }
    return task

@app.route('/todo/tasks', methods=['POST'])
def new_task():
    if (not request.json) or (not ('title' in request.json)):
        abort(400)
    t = makeTask(request.json["title"],request.json.get('description',''))
    tasks.append(t)
    return jsonify({'task':t}), 201


@app.route('/todo/tasks', methods = ['PUT'])
def updateTask():
    if (not request.json) or (not ('id' in request.json)):
        abort(400)
    for task in tasks:
        if task['id'] == request.json["id"]:
            task['description'] = request.json.get('description',task['description'])
            task['done']= request.json.get('done',task['done'])
            task['title'] = request.json.get('title',task['title'])
            return jsonify({'task':task}), 201
    abort(404)

@app.route('/todo/tasks', methods = ['DELETE'])
def delTask():
    if (not request.json) or (not ('id' in request.json)):
        abort(400)
    for task in tasks:
        if task['id'] == request.json["id"]:
            tasks.remove(task)
            return jsonify({'action':'done'}), 201
    abort(400)

if __name__ == '__main__':
    app.run(debug=True)

