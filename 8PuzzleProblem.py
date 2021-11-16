import BasicAiAlgorithms as bi
from copy import deepcopy


"""
    We want to use the greedy algorithm in 8 puzzle problem
    The Goal is like this as the question says
    
    [
        [1, 2, 3],
        [8, " ", 4], 
        [7, 6, 5]
    ] 
    
    [
        [1, 2, 3],
        [6, " ", 4], 
        [7, 8, 5]
    ] 
    So the argument we send is a list consist of three list.
    we have also this for the initial states.
"""

goal = [
                [1, 2, 3],
                [8, " ", 4], 
                [7, 6, 5]
            ]

initial_state = [
                    [1, 2, 3],
                    [6, " ", 4], 
                    [7, 8, 5]
                ] 

current = deepcopy(initial_state)
algo = bi.FormedInformed()
runflag = 1

while goal != current:
    
    if runflag:
        front, expndd, expndd_node = algo.greedyAlgorithm(1, initialState=current, goalState=goal)
        
        print("Goal:")
        for i in goal:
            print(i)
        print("Current state")
        for i in expndd_node:
            print(i)
        runflag = False
    else:
        algo.greedyAlgorithm(0, frontier=front, goalState=goal, expanded=expndd, expanded_node=expndd_node)
        print("Goal:")
        for i in goal:
            print(i)
        print("Current state")
        for i in expndd_node:
            print(i)