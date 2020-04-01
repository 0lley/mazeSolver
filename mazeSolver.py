inpFile = 'mazeInput.txt'

def fileLength(fname):
    i = 0
    for line in open(fname):
        i += 1
    return(i)

def vibeCheck(y, x):
    if y - 1 >= 0 and maze[y-1][x] == 0:
        stack.append(str(y - 1) + str(x))
#CHECKS SQUARES AROUND THE GIVEN ONE AND SENDS AVAILABLE ONES TO THE STACK

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

vibeCheck(int(stack[0][0]), int(stack[0][1]))

print(maze)
print(stack)
print(maze[int(stack[0][0])][int(stack[0][1])])
