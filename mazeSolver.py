inpFle = 'mazeInput.txt'

def fileLength(fname):
    i = 0
    for line in open(fname):
        i += 1
    return(i)

with open(inpFle, 'r') as file:
    data = file.read().replace(', ', '')
    open(inpFle, "w").write(data)
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters

maze = [[x for x in open(inpFle, "r").readline()] for y in range(fileLength(inpFle))] 
#Setting up the actual maze file

for i in range(len(maze)):
    del maze[i][len(maze[i])-1]
#Removes line breaks from the 2d list

print(maze)

# for i in range(5):
#     maze.append(fle.readline())

# for i in range(len(maze)):
#     for j in range(len(maze[i])):
#         print(j)