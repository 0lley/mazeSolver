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

with open(inpFle, 'r') as file:
    data = file.read().replace(', ', '')
    open(inpFle, "w").write(data)
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters

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