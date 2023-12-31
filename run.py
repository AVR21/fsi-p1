# Search methods

import search

#Batería de problemas

ab = search.GPSProblem('A', 'B'
                       , search.romania)

oe = search.GPSProblem('O','E', 
                       search.romania)

gz = search.GPSProblem('G','Z', 
                       search.romania)

nd = search.GPSProblem('N','D', 
                       search.romania)

mf = search.GPSProblem('M','F', 
                       search.romania)



print("Test 1: From Arad to Bucharest")
print("BFS:")
print(search.breadth_first_graph_search(ab).path())
print("DFS:")
print(search.depth_first_graph_search(ab).path())
print("Branch & Bound:")
print(search.branch_and_bound_graph_search(ab).path())
print("Branch & Bound with Subestimation:")
print(search.branch_and_bound_with_subest_graph_search(ab).path())


print("\n---------------------------------------------\n")

print("Test 2: From Oradea to Eforie")
print("BFS:")
print(search.breadth_first_graph_search(oe).path())
print("DFS:")
print(search.depth_first_graph_search(oe).path())
print("Branch & Bound:")
print(search.branch_and_bound_graph_search(oe).path())
print("Branch & Bound with Subestimation:")
print(search.branch_and_bound_with_subest_graph_search(oe).path())

print("\n---------------------------------------------\n")

print("Test 3: From Giurgiu to Zerind")
print("BFS:")
print(search.breadth_first_graph_search(gz).path())
print("DFS:")
print(search.depth_first_graph_search(gz).path())
print("Branch & Bound:")
print(search.branch_and_bound_graph_search(gz).path())
print("Branch & Bound with Subestimation:")
print(search.branch_and_bound_with_subest_graph_search(gz).path())

print("\n---------------------------------------------\n")

print("Test 4: From Neamt to Dobreta")
print("BFS:")
print(search.breadth_first_graph_search(nd).path())
print("DFS:")
print(search.depth_first_graph_search(nd).path())
print("Branch & Bound:")
print(search.branch_and_bound_graph_search(nd).path())
print("Branch & Bound with Subestimation:")
print(search.branch_and_bound_with_subest_graph_search(nd).path())

print("\n---------------------------------------------\n")

print("Test 5: From Mehadia to Fagaras")
print("BFS:")
print(search.breadth_first_graph_search(mf).path())
print("DFS:")
print(search.depth_first_graph_search(mf).path())
print("Branch & Bound:")
print(search.branch_and_bound_graph_search(mf).path())
print("Branch & Bound with Subestimation:")
print(search.branch_and_bound_with_subest_graph_search(mf).path())
