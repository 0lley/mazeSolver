inpFile = 'mazeInput.txt'
stack = []
adjSquares = {}
class completedPath(Exception): pass

def possMoves(y, x):
    adjSquares.clear()
    if y > 0 and maze[y - 1][x] != 1 or 5:
        adjSquares[str(y - 1) + str(x)] = maze[y - 1][x]
    elif y < len(maze) - 1 and maze[y + 1][x] != 1 or 5:
        adjSquares[str(y + 1) + str(x)] = maze[y + 1][x]
    elif x > 0 and maze[y][x - 1] != 1 or 5:
        adjSquares[str(y) + str(x - 1)] = maze[y][x - 1]
    elif x < len(maze[0]) and maze[y][x + 1] != 1 or 5:
        adjSquares[str(y) + str(x + 1)] = maze[y][x + 1]

def move():
    possMoves(int(stack[-1][0]), int(stack[-1][1]))
    if len(adjSquares) == 0:
        del stack[-1]
    if 3 in adjSquares.values():
        print('DONE')
        raise completedPath
    else:
        for i in adjSquares:
            if adjSquares[i] == 0:
                stack.append(i) #
                maze[int(stack[-1][0])][int(stack[-1][1])] = 5
                break

with open(inpFile, 'r') as file:
    data = file.read().replace(', ', ' ')
    open(inpFile, "w").write(data)
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters

with open("mazeInput.txt", "r") as file:
    maze = [[int(i) for i in line.split()] for line in file]
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters user Bartosz Marcinkowski
  
for row, column in enumerate(maze):
    if 5 in column:
        stack.append(str(row) + str(column.index(5)))
#https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

try:
    while True:
        move()
        print(adjSquares)
except completedPath:
    pass

print(maze)
