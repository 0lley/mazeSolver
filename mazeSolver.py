adjSquares = {}
queue = []
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

with open('test_maze1.txt', "r") as file: #Loads the text file into the 2d maze list
    maze = [[int(i) for i in line.replace(',', '').split()] for line in file]

height = len(maze) - 1
width = len(maze[0]) - 1

class completedPath(Exception): pass #Allows for the program to end when the exit is reached

def possMoves(queueElement, notAllowed): #Checks for possible moves from a certain point and adds it to the dictionary adjSquares
    adjSquares.clear()
    y = int(queueElement.split()[0].split(',')[0])
    x = int(queueElement.split()[0].split(',')[1])

    for coord in moves:
        if 0 <= y + coord[0] <= height and 0 <= x + coord[1] <= width and str(maze[y + coord[0]][x + coord[1]]) not in notAllowed: #Checks for traversible tiles in the order: up, down, right, left
            adjSquares[str(y + coord[0]) + ',' + str(x + coord[1])] = maze[y + coord[0]][x + coord[1]] #Adds moveable tiles to the adjSquares dictionary, with its accompanying value (eg 0 or 3)

def move(): #Handles all of the moving of the maze solver
    possMoves(queue[0], '125') #Checks for possible moves and adds the coordinates and tile number to the dictionary adjSquares

    if 3 in adjSquares.values(): #Allows for the loop to end once the solver reaches the maze exit
        raise completedPath

    else: #Carries out the actual process of breadth first search
        for i in adjSquares:
            if i not in queue[0].strip(): #If the tile is unvisited in the current instance, visit it
                queue.append(i + ' ' + queue[0]) #Add the new set of moves to the end of the queue
        queue.pop(0) #Remove the item from the queue, ie mark as complete

for row, column in enumerate(maze): #Searches for and adds the coordinates of the beginning in (y, x) format
    if 5 in column:
        queue.append(str(row) + ',' + str(column.index(5)))
#https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

try: #Executes all of the movement
    while True:
        move()
except completedPath: #Breaks the loop when exception completedPath is raised (when the maze solver reaches the exit)
    pass

for i in queue[0].split(): #The 'winning' combination of moves replaces all traversed 0s with 5s in the maze
    maze[int(i.split(',')[0])][int(i.split(',')[1])] = 5

for line in maze: #Prints out the final resultant maze
    print(str(line).strip('[').strip(']').replace(',', ''))
