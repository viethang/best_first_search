from best_first_search import SearchProblem, SearchNode, BestFirstSearchAlgorithm

states = ['Sibiu', 'Fagaras', 'RV', 'Pitesti', 'Bucharest']
actions = {
  'Sibiu': {'RV': 80, 'Faragas': 99},
  'Faragas': {'Bucharest': 211},
  'RV': {'Pitesti': 97},
  'Pitesti': {'Bucharest': 101}
}

problem = SearchProblem(states, 'Sibiu', 'Bucharest', actions)

criteria = lambda node: node.path_cost
algo = BestFirstSearchAlgorithm(problem, criteria)
result = algo.run()
node = result
path = []
while node is not None:
  path.insert(0, node.state)
  node = node.parent
print("shortest path", path)
print("cost", result.path_cost)