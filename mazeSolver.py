<<<<<<< HEAD
def fileHeight(fname):
    i = 0
    for line in open(fname):
        i += 1
    return(i)
    #Returns amount of rows in maze

def fileWidth(fname):
    i = 0
    for char in open(fname).readline():
        i += 1
    return(i)
# GOTTA WORK FOR THE ACTUAL THINGY

###################################
###################################
##################################

inputFile = 'mazeInput.txt'
=======
fle = open("mazeInput.txt", "r")
maze = [[x for x in range()] for x in range(m)] 

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
#https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
>>>>>>> parent of fe09331... Input stuff

for i in range(5):
    maze.append(fle.readline())

<<<<<<< HEAD
maze = [[x for x in open(inputFile, "r").readline()] for y in range(fileWidth(inputFile))] 

# for row in range(fileHeight('mazeInput.txt')):
#     for column in range(fileWidth('mazeInput.txt')):
#         maze[row][column] = '0'

# with open("mazeInput.txt", 'r') as f:
#     for line in f:
#         lineLis = line.split(',')
#         for char in line.strip():
#             maze[]

print(maze)
=======


for i in range(len(maze)):
    for j in range(len(maze[i])):
        print(j)
>>>>>>> parent of fe09331... Input stuff
