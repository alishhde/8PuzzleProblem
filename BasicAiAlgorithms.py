
class FormedInformed():
    def __init__(self, algorithm):
        pass
    
    def aStarAlgorithm(self):
        pass
    
    def ucsAlgorithm(self):
        pass
    
    def greedyAlgorithm(self, spaceState, initialState=None, frontier=None, expanded=None, GraphSearch=True):
        """
        This method is going to calculate the greedy algorithm. Each time you call this method,
        it define one best next node. So you must repeat calling this method to reach the Goal,
        and you must test the goal in your code after you call this function.

        Args:
            spaceState (a of List two list): This argument is a sequence of all the  states and their costs.
                        first list must be the nodes and the second list must be the cost.
                        
            initialState ([List]): This argument is the start state, we start searching with this argument.
            frontier ([List]): This is a list of the nodes or states that we must choose to expand.
            expanded ([List]): This is also a list of the nodes or states that we have expanded. Defaults to None.
            GraphSearch (bool, optional): This argument define to use the expanded list in our program or not. if this 
                        argument is False then we also change the states that also we have expanded them.
        """
        
        # If we don't want to expand the nodes that are expanded, else Tree search
        if GraphSearch:
            
            if initialState == None:
                return False    # If initial state is empty
            else:
                currentState = initialState
                
                # next_states is consist of the nodes that can move, we must choos the node which has the lowest cost as we are in greedy algoithm
                next_states = self.nextStates(currentState)
                
                # now we must find these nodes cost and choose the node that has lowest cost
                
                #Continue fromm here...
                
                
        else: # When we are using Tree Search algorithm, and we want to also check the nodes that are expanded.
            pass
    
    def nextStates(self, currentState, Problem="8Puzzle"):
        """
        as we are solving 8 puzzle, we describe it here,
            1- First we must find the space in the 8 puzzle.
            2- then we must find the nodes that can change their place,
            3- then we must return these nodes that can move
        """
        pass
    
    def _cost(self, heuristic="NumberOfNotInPlace"):
        pass