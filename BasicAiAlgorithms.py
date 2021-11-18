class FormedInformed():
    def __init__(self):
        pass
    
    def aStarAlgorithm(self):
        pass
    
    def ucsAlgorithm(self):
        pass
    
    def greedyAlgorithm(self, flag=True, spaceState=[], initialState=[], goalState=[], frontier=[], expanded=[], expanded_node=[], GraphSearch=True):
        """
        This method is going to calculate the greedy algorithm. Each time you call this method,
        it define one best next node. So you must repeat calling this method to reach the Goal,
        and you must test the goal in your code after you call this function.

        Args:
            flag (Bool): the first time method call, this must be True
            spaceState (a of List two list): This argument is a sequence of all the  states and their costs.
                        first list must be the nodes and the second list must be the cost, we do not use it 
                        here as we are solving 8 puzzle problem.
                        
            initialState ([List]): This argument is the start state, we start searching with this argument.
            goalState ([List]): This a list consist of three list that each list has the value of a place in 8 puzzle.
            frontier ([List]): This is a list of the nodes or states that we must choose to expand.
            expanded ([List]): This is also a list of the nodes or states that we have expanded. Defaults to None.
            GraphSearch (bool, optional): This argument define to use the expanded list in our program or not. if this 
                        argument is False then we also change the states that also we have expanded them.

        In this method we first create a frontier variable from the initialState, we call the nextStates() method with this variable,
        this mthod will return all the possible states we can have for our next state. 
        After we have defined the next states, we must choose the state which has the lowest cost. the cost of each states compute by the 
        heuristic() method
        """
        
        # If we don't want to expand the nodes that are expanded, else Tree search
        if GraphSearch:
            if flag:
                expanded_node = list()
                expanded.append(initialState)
                expanded_node = initialState
                if frontier == None:
                    return False    # If initial state is empty
                else:
                    # next_states is consist of the nodes that can move, we must choos the node which has the lowest cost as we are in greedy algoithm
                    frontier = self.findNextStates(expanded_node, expanded, frontier) # here we are expanding node with lowest cost
                    # print(frontier, "Thisis line 47", sep="===>" )
                    
                    # now we must find these node's cost and choose the node that has lowest cost
                    heuristicValues = dict()
                    dictOfStates = dict()
                    print("This is frontier line 51 : ", frontier)
                    frontier_index = 0
                    for state in frontier:
                        print("This is current state of frontier line 52", state)
                        keyIsCost = self._cost(state, goalState, heuristic="NumberOfMissPlace")
                        heuristicValues[int(keyIsCost)] = state
                        dictOfStates[frontier_index] = heuristicValues
                        heuristicValues = {}
                        frontier_index += 1
                        
                    print("This is dictOfStates dictionary: ", dictOfStates)
                    
                    # Computing the first minimum cost
                    firstmin = 10
                    for firstDictKey in dictOfStates:
                        for secDictKey_Cost in dictOfStates[firstDictKey]:
                            if secDictKey_Cost < firstmin:
                                firstmin = secDictKey_Cost
                                minstate = dictOfStates[firstDictKey][secDictKey_Cost]
                    nextStateIs = minstate # Here we choose the state which has lowest cost
                    
                    if nextStateIs not in expanded:
                        expanded.append(nextStateIs)
                        expanded_node = nextStateIs
                        # print("This is frontier", frontier)
                        # print(nextStateIs)
                        indexState = frontier.index(nextStateIs)
                        del frontier[indexState]
                        
                    else:
                        while nextStateIs in expanded:
                            del heuristicValues[min(heuristicValues.keys())]
                            nextStateIs = heuristicValues[min(heuristicValues.keys())] # Here we choose the state which has lowest cost
                        else:
                            expanded.append(nextStateIs)
                            expanded_node = nextStateIs
                            indexState = frontier.index(nextStateIs)
                            del frontier[indexState]
                            
                    return frontier, expanded, expanded_node
            else:
                # next_states is consist of the nodes that can move, we must choos the node which has the lowest cost as we are in greedy algoithm
                frontier = self.findNextStates(expanded_node, expanded, frontier) # here we are expanding node with lowest cost
                
                # now we must find these node's cost and choose the node that has lowest cost
                heuristicValues = dict()
                dictOfStates = dict()
                print("This is frontier line 51 : ", frontier)
                frontier_index = 0
                for state in frontier:
                    print("This is current state of frontier line 52", state)
                    keyIsCost = self._cost(state, goalState, heuristic="NumberOfMissPlace")
                    heuristicValues[int(keyIsCost)] = state
                    dictOfStates[frontier_index] = heuristicValues
                    heuristicValues = {}
                    frontier_index += 1
                    
                print("This is dictOfStates dictionary: ", dictOfStates)
                
                # Computing the first minimum cost
                firstmin = 10
                for firstDictKey in dictOfStates:
                    for secDictKey_Cost in dictOfStates[firstDictKey]:
                        if secDictKey_Cost < firstmin:
                            firstmin = secDictKey_Cost
                            minstate = dictOfStates[firstDictKey][secDictKey_Cost]
                nextStateIs = minstate # Here we choose the state which has lowest cost
                
                if nextStateIs not in expanded:
                    expanded.append(nextStateIs)
                    expanded_node = nextStateIs
                    indexState = frontier.index(nextStateIs)
                    del frontier[indexState]
                else:
                    while nextStateIs in expanded:
                        del heuristicValues[min(heuristicValues.keys())]
                        # print("line 98, this is heuristicValues.keys()", heuristicValues.keys())
                        nextStateIs = heuristicValues[min(heuristicValues.keys())] # Here we choose the state which has lowest cost
                    else:
                        expanded.append(nextStateIs)
                        expanded_node = nextStateIs
                        indexState = frontier.index(nextStateIs)
                        del frontier[indexState]
                        
                return frontier, expanded, expanded_node
            
        else: # When we are using Tree Search algorithm, and we want to also check the nodes that are expanded.
            pass
    
    def findNextStates(self, currentState, expanded, frontier, problem="eightPuzzle"):
        """
        as we are solving 8 puzzle, we describe it here,
            1- First we must find the space in the 8 puzzle.
            2- then we must find the nodes that can change their place,
            3- then we must return these nodes that can move
        """
        # print("Here")
        if problem == "eightPuzzle":
            # print("This Here")
            """In 8 puzzle problem, we have a list consist of 3 list each consist of three values e.g.
                [
                    [1, 2, 3],
                    [8, " ", 4], 
                    [7, 6, 5]
                ] 
                In this problem 1- we must find the space and 2- look for the numbers that can change their place
                with space and return those states.
            """
            # 1- We look for the space in the currentState
            rowCounter = 0
            columnCounter = 0
            flag = False
            for eachrow in currentState:
                for value in eachrow:
                    if value == " ":
                        """
                            Now we must find this value's index
                        """
                        spaceIndex = [rowCounter, columnCounter]
                        flag = True # says we must to break
                        break
                    columnCounter += 1
                if flag:
                    flag = False
                    break
                columnCounter = 0
                rowCounter += 1
            # print(spaceIndex, "This is space Index", sep=" ===>  ")
            
            # 2- In the next lines we are going to add all the possible state's index
            availableMoveIndexForSpace = list()
            domain = [0, 1, 2]
            if (rowCounter - 1) in domain:
                availableMoveIndexForSpace.append((rowCounter - 1, columnCounter))

            if (rowCounter + 1) in domain:
                availableMoveIndexForSpace.append((rowCounter + 1, columnCounter))

            if (columnCounter - 1) in domain:
                availableMoveIndexForSpace.append((rowCounter, columnCounter - 1))
                
            if (columnCounter + 1) in domain:
                availableMoveIndexForSpace.append((rowCounter, columnCounter + 1))    
            # print(availableMoveIndexForSpace, "This is available move ", sep=" ==> ")
            
            # 3- Now we must create those states and return all thenext states we have
            from copy import deepcopy
            next_states = [] # each value of this list is complete state
            # print("This is line 162 availableMoveIndexForSpace: ", availableMoveIndexForSpace)
            for moveIndex in availableMoveIndexForSpace:
                # Here we must change the space and the number
                newstate = []
                newstate = deepcopy(currentState)
                # print("this is 166", moveIndex[0], moveIndex[1])
                newstate[rowCounter][columnCounter], newstate[moveIndex[0]][moveIndex[1]] = newstate[moveIndex[0]][moveIndex[1]], newstate[rowCounter][columnCounter]
                
                if newstate in expanded or newstate in frontier:
                    continue
                else:
                    frontier.append(newstate)
            return frontier
                
    def _cost(self, state, goalState, heuristic="NumberOfMissPlace"):
        """This method is going to compute the cost of the givven state.
        Args:
            state (List): It is a list that consist of the 3 list in which we have the values as our problem is 8 puzzle.
            goalState (List):  It is a list that consist of the 3 list in which we have the values as our problem is 8 puzzle.
            heuristic (str, optional): This choose which heuristic method to use. Here we only have NumberOfMissPlace as cost.
            
            as both state and goalState must have the same structure, so we only need to compare the value of the same in index
            in each list.
        """
        if heuristic == "NumberOfMissPlace":
            """ What we have in this heuristic is the number of the numbers in state that are
            not in their right place as that number is in goalstate.
            """
            # print("This is line 182",state, sep="==> ")
            missplace = 0
            for row in range(len(state)):
                for col in  range(len(state)):
                    if state[row][col] != goalState[row][col]:
                        missplace += 1
            return missplace