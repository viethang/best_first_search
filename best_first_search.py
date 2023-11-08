 
class SearchProblem:
  def __init__(self, states, initial_state, goal_state, actions):
    self.states = states
    self.initial_state = initial_state
    self.goal_state = goal_state
    self.actions = actions # actions should be a dict {s1: {s2: c12, s3: c13}]}
    
class SearchNode:
  def __init__(self, state, parent = None, path_cost = 0):
    self.state = state
    self.parent = parent
    self.path_cost = path_cost
    
def expand(node: SearchNode, problem):
  res = []
  s = node.state
  available_actions = problem.actions[s]
  for state in available_actions:
    child = SearchNode(state, node, node.path_cost + available_actions[state])
    res.append(child)
  return res


def insert(frontier: list[SearchNode], node: SearchNode, criteria):
  # suppose that frontier is already sort in descending order under criteria, we simply find the place to insert node
  if len(frontier) == 0:
    frontier.append(node)
  else:
    for i in range(len(frontier)):
      if criteria(frontier[i]) < criteria(node):
        frontier.insert(i, node)
        return
      
    frontier.append(node)
    
class BestFirstSearchAlgorithm:
  def __init__(self, problem: SearchProblem, criteria):
    self.problem = problem
    self.criteria = criteria
    
  def run(self):
    node = SearchNode(self.problem.initial_state)
    frontier = [node]
    reached = {self.problem.initial_state: node} # keep track of the path to the reached states
    while (len(frontier) > 0):
      node = frontier.pop()
      if node.state == self.problem.goal_state:
        return node
      for child in expand(node, self.problem):
        s = child.state
        if s not in reached or reached[s].path_cost > child.path_cost:
          reached[s] = child # update the path to s with the less costly path
          insert(frontier, child, self.criteria)
          
    return 'failed'