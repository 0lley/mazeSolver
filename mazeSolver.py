inpFile = 'mazeInput.txt'
stack = []
adjSquares = {}
class completedPath(Exception): pass

def deleteChar(char, replace): #Replaces characters in the text file
    with open(inpFile, 'r') as file:
        data = file.read().replace(char, replace)
        open(inpFile, "w").write(data)
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters

def possMoves(y, x, notAllowed):
    adjSquares.clear()
    if y > 0 and str(maze[y - 1][x]) not in notAllowed:
        adjSquares[str(y - 1) + str(x)] = maze[y - 1][x]
    if y < len(maze) - 1 and str(maze[y + 1][x]) not in notAllowed:
        adjSquares[str(y + 1) + str(x)] = maze[y + 1][x]
    if x > 0 and str(maze[y][x - 1]) not in notAllowed:
        adjSquares[str(y) + str(x - 1)] = maze[y][x - 1]
    if x < len(maze[0]) - 1 and str(maze[y][x + 1]) not in notAllowed:
        adjSquares[str(y) + str(x + 1)] = maze[y][x + 1]

def move():
    possMoves(int(stack[-1][0]), int(stack[-1][1]), '125')
    if len(adjSquares) == 0:
        del stack[-1]
    if 3 in adjSquares.values():
        print('DONE')
        raise completedPath
    else:
        for i in adjSquares:
            if adjSquares[i] == 0:
                stack.append(str(i))
                maze[int(stack[-1][0])][int(stack[-1][1])] = 5
                break

deleteChar(', ', ' ')

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

with open("mazeInput.txt", "r") as file:
    maze = [[int(i) for i in line.split()] for line in file]

for i in stack:
    maze[int(i[0])][int(i[1])] = 5

with open("mazeInput.txt", "w") as file:
    for row in maze:
        file.write('%s\n' % row)

deleteChar(', ', ' ')
deleteChar('[', ' ')
deleteChar(']', ' ')