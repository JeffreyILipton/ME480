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
    print("in new_task")
    if (not request.json) or (not ('title' in request.json)):
        abort(400)
    t = makeTask(request.json["title"],request.json.get('description',''))
    print(t)
    tasks.append(t)
    print(tasks)
    return jsonify({'task':t}), 201

if __name__ == '__main__':
    app.run(debug=True)

