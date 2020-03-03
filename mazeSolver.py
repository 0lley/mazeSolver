fle = open("mazeInput.txt", "r")
maze = [[x for x in range()] for x in range(m)] 

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
#https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python

for i in range(5):
    maze.append(fle.readline())



for i in range(len(maze)):
    for j in range(len(maze[i])):
        print(j)