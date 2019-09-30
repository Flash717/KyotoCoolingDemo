

class person:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.relationships = []

    def addRelationships(self, relationships):
        if isinstance(relationships, list):
            if len(relationships):
                self.relationships.extend(relationships)

    def countConnections(self, degree = 1):
        level = 0
        connections = { 0: [self]}
        allConnections = [self]
        while level < degree:
            level += 1
            connections[level + 1] = []
            for i in connections[level]:
                if not i in allConnections:
                    connections[level + 1].extend(i)
                    allConnections.extend(i)
