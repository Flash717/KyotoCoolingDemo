from flask import Flask, request
from model.person import person
from model.relationship import relationship

import json

app = Flask(__name__)

app.personList = []
app.relationshipList = []
app.personGraph = {}

@app.route('/')
def index():
    return json.dumps({
        'max': getMax(),
        'min': getMin()
    })

@app.route('/user/<user_id>')
def getUser(user_id = None):
    return str(getUserById(user_id))

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

    connections = getConnections(user_id, degree, allowLoops)
    return str(connections.get(degree))

@app.route('/user/<user_id>/introduction/<other_id>')
def getUserIntroduction(user_id, other_id):
    if not user_id.isnumeric():
        return 'Invalid value for user_id', 400
    if not other_id.isnumeric():
        return 'Invalid value for user_id', 400
    user_id = int(user_id)
    other_id = int(other_id)
    result = introductions(app.personGraph, user_id, other_id)
    return ' -> '.join(str(i) for i in result)

@app.route('/user/<user_id>/common/<other_id>')
def getUserCommonalities(user_id, other_id):
    if not user_id.isnumeric():
        return 'Invalid value for user_id', 400
    if not other_id.isnumeric():
        return 'Invalid value for user_id', 400
    user_id = int(user_id)
    other_id = int(other_id)
    user_a = getUserById(user_id)
    user_b = getUserById(other_id)
    result = list(set(user_a.connections) & set(user_b.connections))
    return str(result)

def initApp():
    app.personList = person.loadPersons('Person.txt')
    app.relationshipList = person.loadRelationships(app.personList, 'Relationship.txt')
    app.personGraph = person.buildGraph(app.personList)

def getUserById(id):
    for i in app.personList:
        if int(i.id) == int(id):
            return i
    return person(0, 'N/A')

def getConnections(user_id, degree=1, allowLoops=False):
    level = 0
    connections = {0: set([user_id])}
    allConnections = set([user_id])
    while level < degree:
        level += 1
        connections[level] = set()
        for i in connections[level-1]:
            p = getUserById(i)
            for j in p.connections:
                if not j in allConnections or allowLoops:
                    connections[level].add(j)
                    allConnections.add(j)
    return connections

def introductions(graph, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if vertex == end:
            return path
        elif vertex not in visited:
            for current_neighbour in graph.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            visited.add(vertex)

def getMax():
    maxVal = max([len(x.connections) for x in app.personList])
    return { 
        'id': [x.id for x in app.personList if len(x.connections) == maxVal],
        'count': maxVal
    }

def getMin():
    minVal = min([len(x.connections) for x in app.personList])
    return {
        'id': [x.id for x in app.personList if len(x.connections) == minVal],
        'count': minVal
    }

if __name__ == '__main__':
    initApp()
    app.run(port=8081)
