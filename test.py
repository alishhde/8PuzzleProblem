

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


# goalState = [
#                 [1, 2, 3],
#                 [8, " ", 4], 
#                 [7, 6, 5]
#             ]

# t = [
#                 [1, 2, 3],
#                 [8, " ", 4], 
#                 [7, 6, 5]
#             ]
# print(t)

dd = {0: {4: ([[1, ' ', 3], [6, 2, 4], [7, 8, 5]], 1)}, 1: {3: ([[1, 2, 3], [6, 8, 4], [7, ' ', 5]], 1)}, 2: {3: [[1, 2, 3], [' ', 6, 4], [7, 8, 5]]}, 3: {4: [[1, 2, 3], [6, 4, ' '], [7, 8, 5]]}}
firstmin = 10
for i in dd:
    for j in dd[i]:
        if j < firstmin:
            firstmin = j
            print(dd[i][j])
            minstate = dd[i][j][0]
        print(j)
    # print(dd[i])

print("\n \n this state", minstate)