import BasicAiAlgorithms as bi
from copy import deepcopy

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
runflag = True
cot = 0

while goal != current:
    
    if runflag:
        front, expndd, expndd_node = algo.greedyAlgorithm(initialState=current, goalState=goal)
        
        print("Goal:")
        for i in goal:
            print(i)
        print("Current state")
        for i in expndd_node:
            print(i)
        runflag = False
    else:
        front, expndd, expndd_node = algo.greedyAlgorithm(flag=False, frontier=front, goalState=goal, expanded=expndd, expanded_node=expndd_node)
        print("\nFrom now we are here ....\n")
        print("Goal:")
        for i in goal:
            print(i)
        print("Current state")
        for i in expndd_node:
            print(i)
            
        if cot == 10:
            break
        cot = cot + 1