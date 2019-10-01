from flask import Flask, request
from model.person import person
from model.personlist import personlist

import json

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({
        'max': app.personList.getMax(),
        'min': app.personList.getMin()
    })

@app.route('/user/<user_id>')
def getUser(user_id = None):
    if not user_id or not app.personList.getUserById(user_id):
        return 'User with id {0} not found'.format(user_id), 404
    result = app.personList.getUserById(user_id)
    return json.dumps({
        'id': result.id,
        'name': result.name,
        'connections': list(result.connections)
    })

@app.route('/user/<user_id>/connections')
def getUserConnections(user_id):
    degree = request.args.get('degree', '1')
    allowLoops = request.args.get('allowLoops', 'False')
    if not degree.isnumeric():
        return 'Invalid value for degree', 400
    if not user_id.isnumeric():
        return 'Invalid value for user_id', 400
    if not allowLoops.lower() in ['true', 'false']:
        return 'Invalid value for allowLoops', 400
    degree = int(degree)
    user_id = int(user_id)
    allowLoops = allowLoops.lower() == 'true'
    if not app.personList.getUserById(user_id):
        return 'User with id {0} not found'.format(user_id), 404

    connections = app.personList.getConnections(user_id, degree, allowLoops)

    return json.dumps({
        'user_id': user_id,
        'degree': degree,
        'connections': list(connections.get(degree)),
        'connection_count': len(connections.get(degree))
    })

@app.route('/user/<user_id>/introduction/<other_id>')
def getUserIntroduction(user_id, other_id):
    if not user_id.isnumeric():
        return 'Invalid value for user_id', 400
    if not other_id.isnumeric():
        return 'Invalid value for user_id', 400
    user_id = int(user_id)
    other_id = int(other_id)
    if not app.personList.getUserById(user_id):
        return 'User with id {0} not found'.format(user_id), 404
    if not app.personList.getUserById(other_id):
        return 'User with id {0} not found'.format(other_id), 404
    result = app.personList.getIntroductions(user_id, other_id)
    return json.dumps({
        'user_a': user_id,
        'user_b': other_id,
        'connection_chain': list(result)
    })

@app.route('/user/<user_id>/common/<other_id>')
def getUserCommonalities(user_id, other_id):
    if not user_id.isnumeric():
        return 'Invalid value for user_id', 400
    if not other_id.isnumeric():
        return 'Invalid value for user_id', 400
    user_id = int(user_id)
    other_id = int(other_id)
    if not app.personList.getUserById(user_id):
        return 'User with id {0} not found'.format(user_id), 404
    if not app.personList.getUserById(other_id):
        return 'User with id {0} not found'.format(other_id), 404
    result = app.personList.getCommonalities(user_id, other_id)
    return json.dumps({
        'user_a': user_id,
        'user_b': other_id,
        'common_connections': list(result)
    })

def initApp():
    # initialization of the person list, relationships and relationship-graph (load files)
    app.personList = personlist.createFromFile('resources/Person.txt')
    app.personList.loadRelationships('resources/Relationship.txt')

if __name__ == '__main__':
    initApp()
    app.run(port=8081)
