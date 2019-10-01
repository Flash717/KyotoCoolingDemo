from model.person import person
from model.relationship import relationship

class personlist:

    def __init__(self):
        self._personList = []
        self._personGraph = {}

    def loadRelationships(self, filename):
        response = []
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                r = line.strip().split(':')
                id = int(r[0])
                relList = [int(x)
                           for x in r[1].split(',') if x.strip().isdigit()]
                for p in self._personList:
                    if p.id == id:
                        p.addConnections(relList)
                for i in relList:
                    response.append(relationship(id, i))
                line = fp.readline()
                
        # now that we have loaded the relationships we can build the graph
        self.buildGraph()

        return response

    def buildGraph(self):
        for i in self._personList:
            self._personGraph[i.id] = i.connections

    def getUserById(self, id):
        for i in self._personList:
            if int(i.id) == int(id):
                return i
        return None

    def getConnections(self, user_id, degree=1, allowLoops=False):
        level = 0
        connections = {0: set([user_id])}
        allConnections = set([user_id])
        while level < degree:
            level += 1
            connections[level] = set()
            for i in connections[level-1]:
                p = self.getUserById(i)
                for j in p.connections:
                    if not j in allConnections or allowLoops:
                        connections[level].add(j)
                        allConnections.add(j)
        return connections

    def getIntroductions(self, start, end):
        queue = [[start]]
        visited = set()

        while queue:
            path = queue.pop(0)
            vertex = path[-1]

            if vertex == end:
                return path
            elif vertex not in visited:
                for current_neighbour in self._personGraph.get(vertex, []):
                    new_path = list(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)

                visited.add(vertex)

    def getMax(self):
        maxVal = max([len(x.connections) for x in self._personList])
        return {
            'id': [x.id for x in self._personList if len(x.connections) == maxVal],
            'count': maxVal
        }


    def getMin(self):
        minVal = min([len(x.connections) for x in self._personList])
        return {
            'id': [x.id for x in self._personList if len(x.connections) == minVal],
            'count': minVal
        }

    def getCommonalities(self, user_a_id, user_b_id):
        user_a = self.getUserById(user_a_id)
        user_b = self.getUserById(user_b_id)
        return list(set(user_a.connections) & set(user_b.connections))

    @staticmethod
    def createFromFile(filename):
        personList = personlist()
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                p = line.strip().split('\t')
                personList._personList.append(person(int(p[0]), p[1]))
                line = fp.readline()

        return personList
