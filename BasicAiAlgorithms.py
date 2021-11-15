
class FormedInformed():
    def __init__(self, algorithm):
        pass
    
    def aStarAlgorithm(self):
        pass
    
    def ucsAlgorithm(self):
        pass
    
    def greedyAlgorithm(self, spaceState, initialState, frontier=None, expanded=None, GraphSearch=True):
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
            
            if initialState not in spaceState:
                return False    # If initial state is empty
            else:
                
                pass
        
        else: # When we are using Tree Search algorithm, and we want to also check the nodes that are expanded.
            pass
        
    def _cost(self, heuristic="NumberOfNotInPlace"):
        pass