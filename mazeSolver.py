inpFile = 'mazeInput.txt'
fileWidth = 7 #MAKE SURE THIS IS AUTOMATIC
adjSquares = {}

def possMoves(y, x):
    if y > 0:
        adjSquares[str(y - 1) + str(x)] = maze[y - 1][x]
    if y < len(maze) - 1:
        adjSquares[str(y + 1) + str(x)] = maze[y + 1][x]
    if x > 0:
        adjSquares[str(y) + str(x - 1)] = maze[y][x - 1]
    if x < len(maze[0]):
        adjSquares[str(y) + str(x + 1)] = maze[y][x + 1]

def move():
    for i in adjSquares:
        if i == 0:
            stack.append(adjSquares[i])
        elif i == 

###################################
###################################
###################################

stack = []

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

possMoves(int(stack[-1][0]), int(stack[-1][1]))
print(adjSquares)

print(maze)
print(stack)
print(int(maze[int(stack[0][0])][int(stack[0][1])]))
