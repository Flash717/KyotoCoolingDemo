from model.relationship import relationship

class person:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.connections = []

    def __repr__(self):
        return 'ID: {0}, Name: {1}, connections: {2}'.format(self.id, self.name, self.connections)

    def addConnections(self, relationships):
        if isinstance(relationships, list):
            if len(relationships):
                self.connections.extend(relationships)

    @staticmethod
    def loadPersons(filename):
        personList = []
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                p = line.strip().split('\t')
                personList.append(person(int(p[0]), p[1]))
                line = fp.readline()

        return personList

    @staticmethod
    def loadRelationships(personList, filename):
        response = []
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                r = line.strip().split(':')
                id = int(r[0])
                relList = [int(x)
                           for x in r[1].split(',') if x.strip().isdigit()]
                for p in personList:
                    if p.id == id:
                        p.addConnections(relList)
                for i in relList:
                    response.append(relationship(id, i))
                line = fp.readline()
        return response

    @staticmethod
    def buildGraph(personList):
        result = {}
        for i in personList:
            result[i.id] = i.connections
        return result
