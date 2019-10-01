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


