# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())

  stack = util.Stack()
  visit = {}
  node = {}
  node["state"] = problem.getStartState()
  node["parent"] = None
  node["action"] = None

  stack.push(node)
  while stack.isEmpty() == False:
    node = stack.pop()
    state = node["state"]
    flag = 0
    "find if there is unpassed node"
    for next in problem.getSuccessors(state):
      if next[0] in visit:
        continue
      else:
        flag = 1
        break

    "already passed and no unpassed node then do next step"
    if state in visit and flag == 0:
        continue
    
    visit[state] = True
    stack.push(node)
    
    "the state is the finish state then end"
    if problem.isGoalState(state) == True:
      break

    "return (successor, action, stepCost)"
    for next in problem.getSuccessors(state):
      if next[0] in visit:
        continue
      else:
        child_node = {}
        child_node["state"] = next[0]
        child_node["parent"] = node
        child_node["action"] = next[1]
        stack.push(child_node)
    
  move = []
  while node["action"] != None:
    move.insert(0, node["action"])
    node = node["parent"]

  return move


def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())

  queue = util.Queue()
  visit = {}
  node = {}
  node["state"] = problem.getStartState()
  node["parent"] = None
  node["action"] = None

  queue.push(node)
  while queue.isEmpty() == False:
    node = queue.pop()
    state = node["state"]
    
    "already passed then do next step"
    if state in visit:
      continue
    visit[state] = True
    
    "the state is the finish state then end"
    if problem.isGoalState(state) == True:
      break

    "return (successor, action, stepCost)"
    for next in problem.getSuccessors(state):
      if next[0] in visit:
        continue
      else:
        child_node = {}
        child_node["state"] = next[0]
        child_node["parent"] = node
        child_node["action"] = next[1]
        queue.push(child_node)

  move = []
  while node["action"] != None:
    move.insert(0, node["action"])
    node = node["parent"]

  return move
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  queue = util.PriorityQueue()
  visit = {}
  node = {}
  node["state"] = problem.getStartState()
  node["parent"] = None
  node["action"] = None
  node["cost"] = 0

  queue.push(node, node["cost"])
  while queue.isEmpty() == False:
    node = queue.pop()
    state = node["state"]
    cost = node["cost"]
    
    "already passed then do next step"
    if state in visit:
      continue
    visit[state] = True
    
    "the state is the finish state then end"
    if problem.isGoalState(state) == True:
      break

    "return (successor, action, stepCost)"
    for next in problem.getSuccessors(state):
      if next[0] in visit:
        continue
      else:
        child_node = {}
        child_node["state"] = next[0]
        child_node["parent"] = node
        child_node["action"] = next[1]
        child_node["cost"] = next[2] + cost
        queue.push(child_node, child_node["cost"])

  move = []
  while node["action"] != None:
    move.insert(0, node["action"])
    node = node["parent"]

  return move

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())

  queue = util.PriorityQueue()
  visit = {}
  node = {}
  node["state"] = problem.getStartState()
  node["parent"] = None
  node["action"] = None
  node["cost"] = 0
  node["estimate"] = heuristic(node["state"], problem)

  queue.push(node, node["cost"] + node["estimate"])
  while queue.isEmpty() == False:
    node = queue.pop()
    state = node["state"]
    cost = node["cost"]
    estimate = node["estimate"]
    
    "already passed then do next step"
    if state in visit:
      continue
    visit[state] = True
    
    "the state is the finish state then end"
    if problem.isGoalState(state) == True:
      break

    "return (successor, action, stepCost)"
    for next in problem.getSuccessors(state):
      if next[0] in visit:
        continue
      else:
        child_node = {}
        child_node["state"] = next[0]
        child_node["parent"] = node
        child_node["action"] = next[1]
        child_node["cost"] = next[2] + cost
        child_node["estimate"] = heuristic(child_node["state"], problem)
        queue.push(child_node, child_node["cost"] + child_node["estimate"])

  move = []
  while node["action"] != None:
    move.insert(0, node["action"])
    node = node["parent"]

  return move
  
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
