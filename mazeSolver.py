inpFile = 'mazeInput.txt'
adjSquares = {}
Queue = {}
PastMoves = {}
class completedPath(Exception): pass

def deleteChar(char, replace): #Replaces characters in the text file
    with open(inpFile, 'r') as file:
        data = file.read().replace(char, replace)
        open(inpFile, "w").write(data)
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters

def keyFromValue(val): #Returns a dictionary key for a chosen value
    return(key for key, value in Queue.items() if value == val)

def possMoves(y, x, notAllowed): #Checks for elligible adjacent tiles
    adjSquares.clear()
    if y > 0 and str(maze[y - 1][x]) not in notAllowed: #Checks for traversible tiles above
        adjSquares[str(y - 1) + str(x)] = maze[y - 1][x]
    elif y < len(maze) - 1 and str(maze[y + 1][x]) not in notAllowed: #Checks for traversible tiles below
        adjSquares[str(y + 1) + str(x)] = maze[y + 1][x]
    elif x > 0 and str(maze[y][x - 1]) not in notAllowed: #Checks for traversible tiles to the left
        adjSquares[str(y) + str(x - 1)] = maze[y][x - 1]
    elif x < len(maze[0]) and str(maze[y][x + 1]) not in notAllowed: #Checks for traversible tiles to the right
        adjSquares[str(y) + str(x + 1)] = maze[y][x + 1]

def move(): #Chooses the moves of the tile
    firstValue = Queue[list(Queue.keys())[0]] #Acquires the value of the first coordinate in the queue
    firstKey = [key for key, value in Queue.items() if value == firstValue][0] #Acquirs the key of the first coordinate in the queue

    possMoves(int(firstKey[0]), int(firstKey[1]), '125') #Retrieves all possible moves for the first item in the queue

    if 3 in adjSquares.values(): #Ends the loop when the path is at the end
        maze[int(firstKey[0])][int(firstKey[1])] = 2
        print('END')
        PastMoves[firstKey] = firstValue #Sends path up to a tile to a dictionary
        raise completedPath

    for i in list(adjSquares.keys()): #Adds all adjacent tiles to the end of the queue
        Queue[i] = firstValue + ' ' + i

    if maze[int(firstKey[0])][int(firstKey[1])] != 5: #Marks used tiles as visited
        maze[int(firstKey[0])][int(firstKey[1])] = 2
    PastMoves[firstKey] = firstValue #Sends path up to a tile to a dictionary
    Queue.pop(firstKey) #Removes tile from queue
    print(Queue)

deleteChar(', ', ' ') #Formats the text file for easy reading by the program

with open("mazeInput.txt", "r") as file:
    maze = [[int(i) for i in line.split()] for line in file]
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters user Bartosz Marcinkowski

for row, column in enumerate(maze):
    if 3 in column:
        exitCoords = str(row) + str(column.index(3))
    if 5 in column:
        Queue[(str(row) + str(column.index(5)))] = str(row) + str(column.index(5))
#https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

try:
    while True:
        move()
        # print(Queue)
        #print(adjSquares)
except completedPath:
    pass

# for i in range(len(PastMoves))

with open("mazeInput.txt", "w") as file:
    for row in maze:
        file.write('%s\n' % row)

print(PastMoves)

deleteChar('[', '')
deleteChar(']', '')
deleteChar(', ', ' ')

print(maze)
