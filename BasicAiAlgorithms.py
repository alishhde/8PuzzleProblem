class FormedInformed():
    
    def aStarAlgorithm(self, flag=True, frontierWithCost={},  indexCounter=0, goalState=[], currentState=[], frontier=[], visited=[], GraphSearch=True):
        """ This function is going to calculate the path to the goal with the A* Algorithm.
        
        Args:
            goalState (list, optional): The goal we are looking for. Defaults to [].
            currentState (list, optional): In the first run it's initial state, then its the current state. Defaults to [].
            frontier (list, optional): All node with the diffrent cost that are not seen yet. Defaults to [].
            visited (list, optional): This is the node we have visited till now. we also use this variable as the expanded state, 
            to prevent repeating it.
            GraphSearch (bool, optional): if its True then we don't expande a node which is already expanded. 
            
        Steps:
            1- we start from initialized state.
            2- we use the next states method to find all next state that we can have.
            3- we calculate the cost to those node from the initial state(Gn). 
            4- we choose the state with the lowest cost.
            5- if this state is not in the visited variable, then we can choose this state.
            6- else we delete this state then choose the next lowest node.(Because of the graphSearch)
        """
        if flag:
            # Finding Frontier Of the Current Node
            visited.append(currentState)
            frontier = self.findNextStates(currentState, visited, frontier)
            
            # Calculating Cost for all of the frontier nodes
            frontierWithCost, frontier, expanded_node, indexCounter = self.frontierToCost(indexCounter, frontier, goalState, visited, solution="AStar")

            # print("This is frontier: ", frontier)
            # print("This is frontierWithCost: ", frontierWithCost)
            # print("This is expanded_node: ", expanded_node)
            # print("This is indexCounter: ", indexCounter)
        
        else:
            # Because frontier has been calculated in the last time so we dont need to calculated it again
            # Calculating Cost for all of the frontier nodes
            
            frontierWithCost, frontier, expanded_node, indexCounter = self.frontierToCost(indexCounter, frontier, goalState, visited, frontCostFlag=False, frontiertoCostDict=frontierWithCost, solution="AStar")
        
        return frontier, visited, currentState, indexCounter, frontierWithCost
    
    def ucsAlgorithm(self, flag=True, frontierWithCost={},  indexCounter=0, goalState=[], currentState=[], frontier=[], visited=[], GraphSearch=True):
        """ This function is going to calculate the path to the goal with the UCS Algorithm. as all we do is similar to
        A* algorithm so we have all of that function with a little change in the self.frontierToCost() method
        
        Args:
            goalState (list, optional): The goal we are looking for. Defaults to [].
            currentState (list, optional): In the first run it's initial state, then its the current state. Defaults to [].
            frontier (list, optional): All node with the diffrent cost that are not seen yet. Defaults to [].
            visited (list, optional): This is the node we have visited till now. we also use this variable as the expanded state, 
            to prevent repeating it.
            GraphSearch (bool, optional): if its True then we don't expande a node which is already expanded. 
            
        Steps:
            1- we start from initialized state.
            2- we use the next states method to find all next state that we can have.
            3- we calculate the cost to those node from the initial state(Gn). 
            4- we choose the state with the lowest cost.
            5- if this state is not in the visited variable, then we can choose this state.
            6- else we delete this state then choose the next lowest node.(Because of the graphSearch)
            
        """
        if flag:
            # Finding Frontier Of the Current Node
            frontier = self.findNextStates(currentState, visited, frontier)
            
            # Calculating Cost for all of the frontier nodes
            indexCounter = 0
            frontierWithCost, frontier, expanded_node, indexCounter = self.frontierToCost(indexCounter, frontier, goalState, visited, solution="UCS")
            
        else:
            # Because frontier has been calculated in the last time so we dont need to calculated it again
            # Calculating Cost for all of the frontier nodes
            frontierWithCost, frontier, expanded_node, indexCounter = self.frontierToCost(indexCounter, frontier, goalState, visited, frontCostFlag=True, frontiertoCostDict=frontierWithCost, solution="UCS")
        

        return frontier, visited, currentState, indexCounter, frontierWithCost
        
    
    
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
                    frontier = []
                    frontier = self.findNextStates(expanded_node, expanded, frontier) # here we are expanding node with lowest cost
                    
                    # now we must find these node's cost and choose the node that has lowest cost
                    heuristicValues = dict()
                    dictOfStates = dict()
                    frontier_index = 0
                    for state in frontier:
                        keyIsCost = self._cost(state, goalState, heuristic="NumberOfMissPlace")
                        # print("this state \n", state, "have this cost: ", keyIsCost)
                        heuristicValues[int(keyIsCost)] = state
                        dictOfStates[frontier_index] = heuristicValues
                        heuristicValues = {}
                        frontier_index += 1
                        
                    # Computing the first minimum cost
                    firstmin = 10
                    for firstDictKey in dictOfStates:
                        for secDictKey_Cost in dictOfStates[firstDictKey]:
                            if secDictKey_Cost < firstmin:
                                firstmin = secDictKey_Cost
                                minstate = dictOfStates[firstDictKey][secDictKey_Cost]
                    nextStateIs = minstate # Here we choose the state which has lowest cost
                    
                    # print("before This is frontier", frontier)
                    # print("before This is expanded", expanded)
                    # print("before This is expanded_node node", expanded_node)
                    
                    if nextStateIs not in expanded:
                        expanded.append(nextStateIs)
                        expanded_node = nextStateIs
                        # print("This is frontier", frontier)
                        # print(nextStateIs)
                        indexState = frontier.index(nextStateIs)
                        del frontier[indexState]
                        
                    else:
                        print("This else has not been checked, \n", nextStateIs, "\n\n\n")
                        while nextStateIs in expanded:
                            del heuristicValues[min(heuristicValues.keys())]
                            nextStateIs = heuristicValues[min(heuristicValues.keys())] # Here we choose the state which has lowest cost
                        else:
                            expanded.append(nextStateIs)
                            expanded_node = nextStateIs
                            indexState = frontier.index(nextStateIs)
                            del frontier[indexState]
                
                    # print("\n\n")
                    # print("After This is frontier", frontier)
                    # print("After This is expanded", expanded)
                    # print("before This is expanded_node node", expanded_node)
                    
                    return frontier, expanded, expanded_node
                
    
            else:
            
                # next_states is consist of the nodes that can move, we must choos the node which has the lowest cost as we are in greedy algoithm
                frontier = []
                frontier = self.findNextStates(expanded_node, expanded, frontier) # here we are expanding node with lowest cost
            
                # now we must find these node's cost and choose the node that has lowest cost
                heuristicValues = dict()
                dictOfStates = dict()
                # print("This is frontier line 51 : ", frontier)
                frontier_index = 0
                for state in frontier:
                    # print("This is current state of frontier line 52", state)
                    keyIsCost = self._cost(state, goalState, heuristic="NumberOfMissPlace")
                    heuristicValues[int(keyIsCost)] = state
                    dictOfStates[frontier_index] = heuristicValues
                    heuristicValues = {}
                    frontier_index += 1
                
                # print("\n\n")
                # print("After This is heuristicValues", heuristicValues)
                # print("After This is dictOfStates", dictOfStates)
                # print("\n\n")
                # raise KeyError
            
            
                # Computing the first minimum cost
                firstmin = 10
                minstate = list()
                for firstDictKey in dictOfStates:
                    for secDictKey_Cost in dictOfStates[firstDictKey]:
                        if secDictKey_Cost < firstmin:
                            firstmin = secDictKey_Cost
                            minstate = dictOfStates[firstDictKey][secDictKey_Cost]
                nextStateIs = minstate # Here we choose the state which has lowest cost
                
                # print("\n\n")
                # print("the first minimum cost", nextStateIs)
                # print("firstmin", firstmin)
                # print("\n\n")
                # raise KeyError
            

                # print("\n\n")
                # print("Before This is expanded states", expanded)
                # print("Before This is expanded_node", expanded_node)
                # print("\n\n")
            
                if nextStateIs not in expanded and nextStateIs != []:
                    expanded.append(nextStateIs)
                    expanded_node = nextStateIs
                    indexState = frontier.index(nextStateIs)
                    del frontier[indexState]
                    
                elif nextStateIs == []:
                    print("all states has been checked")
                    raise KeyError
                else:
                    print("This else has not been checked, \n", nextStateIs, "\n\n\n")
                    while nextStateIs in expanded:
                        del heuristicValues[min(heuristicValues.keys())]
                        # print("line 98, this is heuristicValues.keys()", heuristicValues.keys())
                        nextStateIs = heuristicValues[min(heuristicValues.keys())] # Here we choose the state which has lowest cost
                    else:
                        expanded.append(nextStateIs)
                        expanded_node = nextStateIs
                        indexState = frontier.index(nextStateIs)
                        del frontier[indexState]
                        
                # print("\n\n")
                # print("After This is expanded states", expanded)
                # print("After This is expanded_node", expanded_node)
                # print("\n\n")
                # raise KeyError
                        
                return frontier, expanded, expanded_node
            
        else: # When we are using Tree Search algorithm, and we want to also check the nodes that are expanded.
            pass
    
    ########################################### It is all great till here ################################################
    
    
    def findNextStates(self, currentState, expanded, frontier, problem="eightPuzzle"):
        """
        as we are solving 8 puzzle, we describe it here,
            1- First we must find the space in the 8 puzzle.
            2- then we must find the nodes that can change their place,
            3- then we must return these nodes that can move.
        
        return:
            This functions calculates the frontier nodes and returns it
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
                for col in eachrow:
                    if col == " ":
                        """
                            Now we must find this value's index
                        """
                        spaceIndex = [rowCounter, columnCounter]
                        flag = True # says we must to break
                        break
                    else:
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
            if (spaceIndex[0] - 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0] - 1, spaceIndex[1]))

            if (spaceIndex[0] + 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0] + 1, spaceIndex[1]))

            if (spaceIndex[1] - 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0], spaceIndex[1] - 1))
                
            if (spaceIndex[1] + 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0], spaceIndex[1] + 1))    
            # print(availableMoveIndexForSpace, "This is available move ", sep=" ==> ")
            
            # 3- Now we must create those states and return all thenext states we have
            from copy import deepcopy
            next_states = [] # each value of this list is complete state
            # print("This is line 162 availableMoveIndexForSpace: ", availableMoveIndexForSpace)
            
            # frontier = [] # This line resets frontier so we dont have the frontier of the last state we passed
            # we did the last line in the greedy itself
            self.newnodes = []
            for moveIndex in availableMoveIndexForSpace:
                # Here we must change the space and the number
                newstate = []
                newstate = deepcopy(currentState)
                # print("this is 166", moveIndex[0], moveIndex[1])
                newstate[spaceIndex[0]][spaceIndex[1]], newstate[moveIndex[0]][moveIndex[1]] = newstate[moveIndex[0]][moveIndex[1]], newstate[spaceIndex[0]][spaceIndex[1]]
                
                if newstate in expanded or newstate in frontier:
                    continue
                else:
                    self.newnodes.append(newstate)
                    frontier.append(newstate)
            # print("This is frontier", frontier)
            
            return frontier # A list of all the next states
                
    def _cost(self, state, goalState, heuristic="NumberOfMissPlace"):
        """This method is going to compute the cost of the given state. 
        It takes a single state as input and returns it cost.
        
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
        
    def frontierToCost(self, indexCounter, frontier, goalState, visited, frontCostFlag=True, frontiertoCostDict={}, solution="AStar"):
        """This method takes the frontier which contains all the next state, as input 
        and returns a dictionary which contains the next nodes with their cost

        Args:
            frontier ([type]): [description]
        """
        if solution == "AStar":
            
            
            # Calculating heuristic and real cost
            if frontCostFlag:
                for state in frontier:
                    heur = self._cost(state, goalState)
                    frontiertoCostDict[indexCounter] = {heur:(state, 1)}
                    indexCounter += 1
            
            # print("This is frontier: ", frontier)
            # print("This is frontiertoCostDict: ", frontiertoCostDict)
            # raise ValueError
        
        
            # Choosing the minimum
            firstmin = 10
            for firstDictKey in frontiertoCostDict:
                for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                    if secDictKey_Cost < firstmin:
                        firstmin = secDictKey_Cost
                        minstate = frontiertoCostDict[firstDictKey][secDictKey_Cost]
                        
            nextStateIs = minstate[0] # Here we choose the state which has lowest cost
            nextStateCostIs = minstate[1]
            
            print("this is nextstate ", nextStateIs)
            
            index = frontier.index(nextStateIs)
            del frontier[0]
            
            # print("This is frontier after deleted visited: ", frontier)
            # print("This is nextStateIs: ", nextStateIs)
            # raise ValueError
        
############################### AALLL Greate ##########################
            # print("This is visited: ", visited)
            # print("This is nextStateIs: ", nextStateIs)
        
            if nextStateIs not in visited:
                visited.append(nextStateIs)
                expanded_node = nextStateIs
                # we must compute the next state of this node and expand them(Add them to the frontiertoCostDict)
                nextOfTheExpandedNode = self.findNextStates(expanded_node, visited, frontier)
                # print("nextOfTheExpandedNode ", nextOfTheExpandedNode)
                # we must delete this node from the frontiertoCostDict and also frontier
                # indexState = frontier.index(nextStateIs)
                # del frontier[indexState]
                
                # print("This is visited: ", visited)
                # print("This is frontier: ", frontier)
                # print("This is self.newnodes: ", self.newnodes)
                # print("This is nextOfTheExpandedNode: ", nextOfTheExpandedNode)
                # raise ValueError
                
                ToRemoveValue = []
                for firstDictKey in frontiertoCostDict:
                    for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                        if frontiertoCostDict[firstDictKey][secDictKey_Cost][0] == nextStateIs:
                            ToRemoveValue.append(firstDictKey)
                            # del frontiertoCostDict[firstDictKey][secDictKey_Cost] # we did it in the next line
                            
                for removeState in ToRemoveValue:
                    del frontiertoCostDict[removeState]

                print(frontiertoCostDict, "\n\n\n")
                # raise ValueError
                
                # Adding next of the expanded node to the list 
                for state in self.newnodes:
                    heurisCost = self._cost(state, goalState)
                    Fn = nextStateCostIs + heurisCost
                    frontiertoCostDict[indexCounter] = {Fn:(state, nextStateCostIs+1)}
                    indexCounter += 1
                
                print(frontiertoCostDict, "\n\n\n")
                raise ValueError
                
            else:
                print("This else has not been checked")
                raise ValueError
                
                while nextStateIs in visited:
                    
                    # First delete the next state because it has been visited
                    ToRemoveValue = []
                    for firstDictKey in frontiertoCostDict:
                        for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                            if frontiertoCostDict[firstDictKey][secDictKey_Cost][0] == nextStateIs:
                                ToRemoveValue.append(firstDictKey)
                                # del frontiertoCostDict[firstDictKey][secDictKey_Cost]

                    for removeState in ToRemoveValue:
                        del frontiertoCostDict[removeState]
                    
                    # then choose the lowest cost from the remaining states 
                    firstmin = 10
                    for firstDictKey in frontiertoCostDict:
                        for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                            if secDictKey_Cost < firstmin:
                                firstmin = secDictKey_Cost
                                minstate = frontiertoCostDict[firstDictKey][secDictKey_Cost]
                    nextStateIs = minstate[0] # Here we choose the state which has lowest cost
                    nextStateCostIs = minstate[1]
            
                else:
                    visited.append(nextStateIs)
                    expanded_node = nextStateIs
                    
                    # we must compute the next state of this node and expand them(Add them to the frontiertoCostDict)
                    nextOfTheExpandedNode = self.findNextStates(expanded_node, visited, frontier)
                
                    # we must delete this node from the frontiertoCostDict and also frontier
                    # indexState = frontier.index(nextStateIs)
                    # del frontier[indexState]
                    
                    ToRemoveValue = []
                    for firstDictKey in frontiertoCostDict:
                        for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                            if frontiertoCostDict[firstDictKey][secDictKey_Cost][0] == nextStateIs:
                                ToRemoveValue.append((firstDictKey, secDictKey_Cost))
                                # del frontiertoCostDict[firstDictKey][secDictKey_Cost]
                                
                    for removeState in ToRemoveValue:
                        del frontiertoCostDict[removeState[0]][removeState[1]]
                        
                    # Adding next of the expanded node to the list 
                    for state in nextOfTheExpandedNode:
                        heurisCost = self._cost(state, goalState)
                        Fn = nextStateCostIs + heurisCost
                        frontiertoCostDict[indexCounter] = {Fn:(state, nextStateCostIs+1)}
                        indexCounter += 1
            return frontiertoCostDict, nextOfTheExpandedNode, expanded_node, indexCounter
        
        elif solution == "UCS":
            
            if frontCostFlag:
                for state in frontier:
                    frontiertoCostDict[indexCounter] = {1:state}
                    indexCounter += 1
                
            
            firstmin = 10
            for firstDictKey in frontiertoCostDict:
                for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                    if secDictKey_Cost < firstmin:
                        firstmin = secDictKey_Cost
                        minstate = frontiertoCostDict[firstDictKey][secDictKey_Cost]
            nextStateIs = minstate # Here we choose the state which has lowest cost
            nextStateCostIs = firstmin
            
            if nextStateIs not in visited:
                visited.append(nextStateIs)
                expanded_node = nextStateIs
                
                # we must compute the next state of this node and expand them(Add them to the frontiertoCostDict)
                nextOfTheExpandedNode = self.findNextStates(expanded_node, visited, frontier)
                
                # we must delete this node from the frontiertoCostDict and also frontier
                indexState = frontier.index(nextStateIs)
                del frontier[indexState]
                
                ToRemoveValue = []
                for firstDictKey in frontiertoCostDict:
                    for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                        if frontiertoCostDict[firstDictKey][secDictKey_Cost] == nextStateIs:
                            ToRemoveValue.append((firstDictKey, secDictKey_Cost))
                            # del frontiertoCostDict[firstDictKey][secDictKey_Cost]
                            
                for removeState in ToRemoveValue:
                    del frontiertoCostDict[removeState[0]][removeState[1]]
                
                # Adding next of the expanded node to the list 
                for state in nextOfTheExpandedNode:
                    frontiertoCostDict[indexCounter] = {nextStateCostIs+1:state}
                    indexCounter += 1
                    
            else:
                while nextStateIs in visited:
                    
                    # First delete the next state because it has been visited
                    ToRemoveValue = []
                    for firstDictKey in frontiertoCostDict:
                        for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                            if frontiertoCostDict[firstDictKey][secDictKey_Cost] == nextStateIs:
                                ToRemoveValue.append((firstDictKey, secDictKey_Cost))
                                # del frontiertoCostDict[firstDictKey][secDictKey_Cost]
                    
                    for removeState in ToRemoveValue:
                        del frontiertoCostDict[removeState[0]][removeState[1]]
                    
                    # then choose the lowest cost from the remaining states 
                    firstmin = 10
                    for firstDictKey in frontiertoCostDict:
                        for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                            if secDictKey_Cost < firstmin:
                                firstmin = secDictKey_Cost
                                minstate = frontiertoCostDict[firstDictKey][secDictKey_Cost]
                    nextStateIs = minstate # Here we choose the state which has lowest cost
                    nextStateCostIs = firstmin
            
                else:
                    visited.append(nextStateIs)
                    expanded_node = nextStateIs
                    
                    # we must compute the next state of this node and expand them(Add them to the frontiertoCostDict)
                    nextOfTheExpandedNode = self.findNextStates(expanded_node, visited, frontier)
                
                    # we must delete this node from the frontiertoCostDict and also frontier
                    indexState = frontier.index(nextStateIs)
                    del frontier[indexState]
                    
                    ToRemoveValue = []
                    for firstDictKey in frontiertoCostDict:
                        for secDictKey_Cost in frontiertoCostDict[firstDictKey]:
                            if frontiertoCostDict[firstDictKey][secDictKey_Cost] == nextStateIs:
                                ToRemoveValue.append((firstDictKey, secDictKey_Cost))
                                # del frontiertoCostDict[firstDictKey][secDictKey_Cost]
                                
                    for removeState in ToRemoveValue:
                        del frontiertoCostDict[removeState[0]][removeState[1]]
                    
                    # Adding next of the expanded node to the list 
                    for state in nextOfTheExpandedNode:
                        frontiertoCostDict[indexCounter] = {nextStateCostIs+1:state}
                        indexCounter += 1
                                
            return frontiertoCostDict, frontier, expanded_node, indexCounter
            
    
    