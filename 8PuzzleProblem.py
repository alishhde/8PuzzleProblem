import BasicAiAlgorithms as bi
from copy import deepcopy
from time import sleep

goal = [
                [1, 2, 3],
                [8, " ", 4], 
                [7, 6, 5]
            ]

initial_state = [
                    [2, 8, 3],
                    [1, 6, 4], 
                    [7, " ", 5]
                ] 

for i in initial_state:
    print(i)

algo = bi.FormedInformed()
runflag = True
cot = 0

while goal != initial_state:
    
    if runflag: # Only in the first run
        # front, expndd, expndd_node = algo.greedyAlgorithm(initialState=initial_state, goalState=goal)
        front, expndd, expndd_node, indexCount, frontierWithCos = algo.aStarAlgorithm(currentState=initial_state, goalState=goal)
        # front, expndd, expndd_node,indexCount, frontierWithCos = algo.ucsAlgorithm(currentState=initial_state, goalState=goal)
        
        # print("Goal:")
        # for i in goal:
        #     print(i)
        # print("Current state")
        for i in expndd_node:
            print(i)
        initial_state = expndd_node
        runflag = False
    else:
        # front, expndd, expndd_node = algo.greedyAlgorithm(flag=False, frontier=front, goalState=goal, expanded=expndd, expanded_node=expndd_node)
        front, expndd, expndd_node, indexCount, frontierWithCos = algo.aStarAlgorithm(flag=False, frontierWithCost=frontierWithCos, indexCounter=indexCount, frontier=front, goalState=goal, visited=expndd, currentState=expndd_node)
        # front, expndd, expndd_node, indexCount, frontierWithCos = algo.ucsAlgorithm(flag=False, frontierWithCost=frontierWithCos, indexCounter=indexCount, frontier=front, goalState=goal, visited=expndd, currentState=expndd_node)
        
        # print("\nFrom now we are here ....\n")
        # print("Goal:")
        # for i in goal:
        #     print(i)
        print("Current state")
        for i in expndd_node:
            print(i)
        # sleep(0.5)
        initial_state = expndd_node
        if cot == 1000:
            print(cot)
            break
        cot = cot + 1
else:
    print("DONE!")