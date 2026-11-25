# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
      
    # Initialization of the frontier from util.py and the start state of the problem
    frontier = util.Stack()
    # initialization of visited to Keep track of visited states for Graph Search using an empty set()
    visited =set ()
    # Push starting node using a tuple of (state, path_of_actions) onto the stack
    start_state = problem.getStartState()
    frontier.push((start_state, [])) 
    #Loop while stack is not empty 
    while not frontier.isEmpty():
        #pop the most recently added node (LIFO) in terms of state and action(path)
        current_state, actions = frontier.pop()
        # skip if already expanded to avoid duplicate
        if current_state in visited: 
            continue
         # Mark as visited upon expansion (pop)
        visited.add(current_state)
        # Check if we reached the goal upon popping and return if true
        if problem.isGoalState(current_state):
            return actions
        # Expand only the unvisited state by checking if current state not in visited set and add if not
        if current_state not in visited:
            visited.add(current_state)
             # Go through the loop pulling the next state using problem.getSuccessor(current_state) in terms of state, action and cost 
        for next_state, action, step_cost in (problem.getSuccessors(current_state)):
                 # Push onto the stack if next_state not in visited
                if next_state not in visited:
                    new_actions = actions + [action]
                    frontier.push((next_state, new_actions))            
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
   
# must import the object named queue from util.py to be to use queue data structure
    from util import Queue
 # Initialization of the frontier with a queue from util.py and the start state of the problem
    frontier = Queue()
    start_state = problem.getStartState()
    # initialization of examined to Keep track of visited states for Graph Search using an empty set()
    examined =set ()
    # Push starting node using a tuple of (state, path_of_actions) onto the queue
    frontier.push((start_state, [])) 
    #visited.add(start_state)
    #Loop while queue is not empty 
    while not frontier.isEmpty():
        #pop the first added node (FIFO) in terms of state and action(path)
        current_state, actions = frontier.pop()
        # skip if already expanded to avoid duplicate
       
        if current_state in examined:
            continue
         # Mark as examined upon expansion (pop)
        examined.add(current_state)
        # Check if we reached the goal upon popping and return if true
        if problem.isGoalState(current_state):
            return actions
        # Go through the loop pulling the next state using problem.getSuccessor(current_state) in terms of state, action and cost 
        for next_state, action, step_cost in (problem.getSuccessors(current_state)):
                 # Push onto the stack if next_state not in visited
                if next_state not in examined:
                    new_actions = actions + [action]
                    frontier.push((next_state, new_actions))            
    return []


def uniformCostSearch (problem):
    """Search the node of least total cost first."""
    #Define cost funtion from util.py
    cost_funtion = lambda item:item[2]
    #Initialize frontier using Priority queue with a function determined by the 3rd element of the tuple: cumulative cost
    frontier = util.PriorityQueueWithFunction (cost_funtion)
    # initialization of visited to Keep track of visited states for Graph Search using an empty set()
    visited =set() 
    # Push starting node using a tuple of (state, path_of_actions and cost) onto the stack
    start_state = problem.getStartState()
    frontier.push((start_state,[],0))
    #Loop while priority queue is not empty 
    while not frontier.isEmpty():
        #pop the least recently added node (FIFO) in terms of state and action(path)
        current_state, actions, current_cost = frontier.pop()
        # Check if we reached the goal upon popping and return if true
        if problem.isGoalState(current_state):
            return actions
        # skip if already expanded to avoid duplicate
        if current_state in visited:
            continue
        # Expand only the unvisited state by checking if current state not in visited set and add if not
        if current_state not in visited:
        # Mark as visitied upon expansion (pop)
            visited.add(current_state)
        # Go through the loop pulling the next state using problem.getSuccessor(current_state) in terms of state, action and accumalated cost 
            for next_state, action, step_cost in problem.getSuccessors(current_state):
         # Push onto the stack if next_state not in visited, so only expand univisited staes [Graph search]
             if next_state not in visited:
                new_actions = actions + [action]
                new_cost = current_cost + step_cost
                frontier.push((next_state, new_actions, new_cost))

    return []
 
    """
        A heuristic function estimates the cost from the current state to the nearest
         goal in the provided SearchProblem. The Manhattan distance heuristic for a PositionSearchProblem
         """  

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is best used to pass the 
    autograder which uses graph search
    """
    return 0

# In orde to pass the upgrader This manhattan distance cannot be hardcoded
# Rather call the passed-in heuristic argument rather than directly.
# Added as reference. 
""""     
def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])"""

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    frontier = PriorityQueue()
    start_state = problem.getStartState()
    # Push tuple: (state, path_of_actions, cost_so_far) with priority Optimal_cost[f] = cost_so_far[g] + heuristic[h]
    frontier.push((start_state, [], 0), heuristic(start_state, problem))
    explored = {} # Stores lowest cost_so_far found for each visited state

    while not frontier.isEmpty():
        state, actions, cost_so_far = frontier.pop()

        if problem.isGoalState(state):
            return actions

        # Only expand if this state hasn't been reached via a cheaper path
        if state not in explored or cost_so_far < explored[state]:
            explored[state] = cost_so_far
            for next_state, action, step_cost in problem.getSuccessors(state):
                new_cost_so_far = cost_so_far + step_cost
                optimal_cost = new_cost_so_far + heuristic(next_state, problem)
                frontier.push((next_state, actions + [action], new_cost_so_far), optimal_cost)
                
    return []

   
   
    
   

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
