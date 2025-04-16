from route import Route

route1 = Route('k0', (2, 3))

if route1.graph.number_of_nodes() != 1:
    raise ValueError('Expected 1 node')
else:
    print('Test 1 passed: Graph initialized with 1 node')

route1.add_stop('5', (10, 3))

if route1.graph.number_of_nodes() != 2:
    raise ValueError('Expected 2 nodes')
else:
    print('Test 2 passed: node added')

if route1.obj != 8:
    raise ValueError('Expected weight equals 8')
else:
    print('Test 3 passed: correct weight')

route1.add_stop('3', (9, -4))

if route1.graph.number_of_nodes() != 3:
    raise ValueError('Expected 3 nodes')
else:
    print('Test 4 passed: node added')

if route1.obj != 15:
    raise ValueError('Expected weight equals 15')
else:
    print('Test 5 passed: correct weight')

if route1.trajectory != ['0', '5', '3']:
    raise ValueError('Expected trajectory equals [0, 5, 3]')
else:
    print('Test 6 passed: correct trajectory')

route1.add_stop('4', (-1, 6))

if route1.graph.number_of_nodes() != 4:
    raise ValueError('Expected 4 nodes')
else:
    print('Test 7 passed: node added')

if route1.obj != 29:
    raise ValueError('Expected weight equals 29')
else:
    print('Test 8 passed: correct weight')

if route1.trajectory != ['0', '5', '3', '4']:
    raise ValueError('Expected trajectory equals [0, 5, 3, 4]')
else:
    print('Test 9 passed: correct trajectory')

route1.remove_stop('3')

if route1.graph.number_of_nodes() != 3:
    raise ValueError('Expected 3 nodes')
else:
    print('Test 10 passed: node removed')

if route1.obj != 19:
    raise ValueError('Expected weight equals 19')
else:
    print('Test 11 passed: correct weight')

if route1.trajectory != ['0', '5', '4']:
    raise ValueError('Expected trajectory equals [0, 5, 4]')
else:
    print('Test 12 passed: correct trajectory')

route1.remove_stop('4')

if route1.graph.number_of_nodes() != 2:
    raise ValueError('Expected 2 nodes')
else:
    print('Test 13 passed: node removed')

if route1.obj != 8:
    raise ValueError('Expected weight equals 8')
else:
    print('Test 14 passed: correct weight')

if route1.trajectory != ['0', '5']:
    raise ValueError('Expected trajectory equals [0, 5]')
else:
    print('Test 15 passed: correct trajectory')


