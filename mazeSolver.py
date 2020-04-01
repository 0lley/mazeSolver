inpFile = 'mazeInput.txt'

def fileLength(fname):
    i = 0
    for line in open(fname):
        i += 1
    return(i)

###################################
###################################
###################################

with open(inpFile, 'r') as file:
    data = file.read().replace(', ', ' ')
    open(inpFile, "w").write(data)

with open("mazeInput.txt", "r") as file:
    maze = [[int(i) for i in line.split()] for line in file]
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters user Bartosz Marcinkowski

print(maze)