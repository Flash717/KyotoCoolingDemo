from model.person import person

test_name = 'Test'
test_id = 1
test_connections = [2,3,4]

def test_person():

    p = person(test_id, test_name)
    assert(p is not None)
    assert(test_id == p.id)
    assert(test_name == p.name)
    assert(len(p.connections) == 0)

def test_person_addconnections():
    p = person(test_id, test_name)
    p.addConnections(test_connections)
    assert(p is not None)
    assert(p.connections is not None)
    assert(len(p.connections) == len(test_connections))
