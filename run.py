# Search methods

import search



ab = search.GPSProblem('A', 'B'
                       , search.romania)

#Batería de tests

oe = search.GPSProblem('O','E', 
                       search.romania)

gz = search.GPSProblem('G','Z', 
                       search.romania)

nd = search.GPSProblem('N','D', 
                       search.romania)

mf = search.GPSProblem('M','F', 
                       search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
