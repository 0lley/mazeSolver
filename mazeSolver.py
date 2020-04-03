inpFile = 'test_maze1.txt'
adjSquares = {}
Queue = []
class completedPath(Exception): pass #Allows for the program to end when the exit is reached

def formatFile(char1, char2):
    with open(inpFile, 'r') as file:
        data = file.read().replace(char1, char2)
        open(inpFile, "w").write(data)
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters

def possMoves(y, x, notAllowed):
    adjSquares.clear()
    if y > 0 and str(maze[y - 1][x]) not in notAllowed: #Checks if the tile above is traversible
        adjSquares[str(y - 1) + str(x)] = maze[y - 1][x]
        
    if y < len(maze) - 1 and str(maze[y + 1][x]) not in notAllowed: #Checks if the tile below is traversible
        adjSquares[str(y + 1) + str(x)] = maze[y + 1][x]

    if x > 0 and str(maze[y][x - 1]) not in notAllowed: #Checks if the tile 
        adjSquares[str(y) + str(x - 1)] = maze[y][x - 1]

    if x < len(maze[0]) - 1 and str(maze[y][x + 1]) not in notAllowed:
        #if str(maze[y][x + 1]) not in Queue[0].strip():
        adjSquares[str(y) + str(x + 1)] = maze[y][x + 1]

def move(): ###FIX THIS UP SO IT GOES FROM 3 TO 5
    possMoves(int(Queue[0][0]), int(Queue[0][1]), '12')

    if len(adjSquares) == 0:
        Queue.pop(0)

    elif 3 in adjSquares.values():
        print('DONE')
        raise completedPath

    else:
        for i in adjSquares:
            if i in Queue[0].strip():
                continue
            else:
                Queue.append(i + ' ' + Queue[0])
        Queue.pop(0)

formatFile(', ', ' ')

with open(inpFile, "r") as file:
    maze = [[int(i) for i in line.split()] for line in file]
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters user Bartosz Marcinkowski
  
for row, column in enumerate(maze):
    if 5 in column:
        Queue.append(str(row) + str(column.index(5)))
#https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

try:
    while True:
        move()
except completedPath:
    pass

for i in Queue.pop(0).split():
    maze[int(i[0])][int(i[1])] = 5

print(maze)

#(PassMoves)