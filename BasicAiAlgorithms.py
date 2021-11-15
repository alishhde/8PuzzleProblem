
class FormedInformed():
    def __init__(self, algorithm):
        pass
    
    def aStarAlgorithm(self):
        pass
    
    def ucsAlgorithm(self):
        pass
    
    def greedyAlgorithm(self, spaceState, initialState, frontier=None, expanded=None, GraphSearch=True):
        """
        This method is going to calculate the greedy algorithm.

        Args:
            spaceState (List): This argument is a sequence of all the  states that we have.
            initialState ([List]): This argument is the start state, we start searching with this argument.
            frontier ([List]): This is a list of the nodes or states that we must choose to expand.
            expanded ([List]): This is also a list of the nodes or states that we have expanded. Defaults to None.
            GraphSearch (bool, optional): This argument define to use the expanded list in our program or not. if this 
                        argument is False then we also change the states that also we have expanded them.
        """
        
        # If we don't want to expand the states that are expanded
        if GraphSearch:
            pass
        
    