from model.personlist import personlist

"""
It is assumed for following unit tests that proper files
resources/Person.txt and
resources/Relationship.txt
exist
"""

def test_personlist_createFromFile_and_getUserById():
    pl = personlist.createFromFile('resources/Person.txt')
    # unit test for createFromFile
    assert(pl is not None)
    assert(len(pl._personList) > 0)
    p = pl.getUserById(1)
    # unit test for getUserById
    assert(p is not None)
    assert(p.id is not None)
    assert(p.name is not None)

def test_loadRelationships():
    pl = personlist.createFromFile('resources/Person.txt')
    pl.loadRelationships('resources/Relationship.txt')
    assert(pl.getUserById(1) is not None)
    p = pl.getUserById(1)
    assert(p.connections is not None)
    assert(len(p.connections) > 0)

def test_buildGraph():
    pl = personlist.createFromFile('resources/Person.txt')
    # initially empty
    assert(pl._personGraph == {})
    pl.loadRelationships('resources/Relationship.txt')
    # next line is actually called in loadRelationships but called here explicitly
    pl.buildGraph()
    assert(pl._personGraph is not None)
    assert(len(pl._personGraph) > 0)

def test_getConnections():
    pl = personlist.createFromFile('resources/Person.txt')
    pl.loadRelationships('resources/Relationship.txt')
    connections = pl.getConnections(1)
    assert(connections is not None)
    assert(len(connections) > 0)

def test_getIntroductions():
    pl = personlist.createFromFile('resources/Person.txt')
    pl.loadRelationships('resources/Relationship.txt')
    path = pl.getIntroductions(1, 2)
    assert(path is not None)
    assert(len(path) > 0)

def test_getMax():
    pl = personlist.createFromFile('resources/Person.txt')
    pl.loadRelationships('resources/Relationship.txt')
    maxVal = pl.getMax()
    assert(maxVal is not None)
    assert(maxVal.get('id') is not None)
    assert(maxVal.get('count') is not None)
    assert(maxVal.get('count') > 0)

def test_getMin():
    pl = personlist.createFromFile('resources/Person.txt')
    pl.loadRelationships('resources/Relationship.txt')
    minVal = pl.getMin()
    assert(minVal is not None)
    assert(minVal.get('id') is not None)
    assert(minVal.get('count') is not None)
    assert(minVal.get('count') > 0)

def test_getCommonalities():
    pl = personlist.createFromFile('resources/Person.txt')
    pl.loadRelationships('resources/Relationship.txt')
    result = pl.getCommonalities(1, 2)
    assert(result is not None)
    assert(len(result) > 0)
