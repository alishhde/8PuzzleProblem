

# rowCounter, columnCounter = 1, 1


# availableMoveForSpace = list()
# print(f"This is available moves: {availableMoveForSpace}")
# domain = [0, 1, 2]
# if (rowCounter - 1) in domain:
#     availableMoveForSpace.append((rowCounter - 1, columnCounter))

# if (rowCounter + 1) in domain:
#     availableMoveForSpace.append((rowCounter + 1, columnCounter))

# if (columnCounter - 1) in domain:
#     availableMoveForSpace.append((rowCounter, columnCounter - 1))
    
# if (columnCounter + 1) in domain:
#     availableMoveForSpace.append((rowCounter, columnCounter + 1))  

# print(f"This is available moves: {availableMoveForSpace}")
# print(f"This is available moves: {availableMoveForSpace[0][0]}")


heuristicValues = {
    1: "num 1",
    2: "num 2",
    0: "num 3"
}


nextStateIs = heuristicValues[min(heuristicValues.keys())]
print(nextStateIs)
