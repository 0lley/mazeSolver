inpFile = 'test_maze1.txt'
adjSquares = {}
Queue = []

class completedPath(Exception): pass #Allows for the program to end when the exit is reached

def possMoves(y, x, notAllowed): #Checks for possible moves from a certain point and adds it to the dictionary adjSquares
    adjSquares.clear()

    if y > 0 and str(maze[y - 1][x]) not in notAllowed: #Checks if the tile above is traversible
        adjSquares[str(y - 1) + str(x)] = maze[y - 1][x]
        
    if y < len(maze) - 1 and str(maze[y + 1][x]) not in notAllowed: #Checks if the tile below is traversible
        adjSquares[str(y + 1) + str(x)] = maze[y + 1][x]

    if x > 0 and str(maze[y][x - 1]) not in notAllowed: #Checks if the tile to the left is traversible
        adjSquares[str(y) + str(x - 1)] = maze[y][x - 1]

    if x < len(maze[0]) - 1 and str(maze[y][x + 1]) not in notAllowed: #Checks if the tile to the right is traversible
        adjSquares[str(y) + str(x + 1)] = maze[y][x + 1]

def move(): #Handles all of the moving of the maze solver
    possMoves(int(Queue[0][0]), int(Queue[0][1]), '12') #Checks for possible moves and adds the coordinates and tile number to the dictionary adjSquares

    if len(adjSquares) == 0: #Removes the branch of the tree if it reaches a dead end
        Queue.pop(0)

    elif 3 in adjSquares.values(): #Allows for the loop to end once it the solver reaches the maze exit
        raise completedPath

    else: #Carries out the actual process of breadth first search
        for i in adjSquares:
            if i in Queue[0].strip(): #If the tile has been visited before in the current instance, go onto the next adjacent tile
                continue
            else: #If the tile is unvisited in the current instance, visit it
                Queue.append(i + ' ' + Queue[0]) #Add the new set of moves to the end of the queue
        Queue.pop(0) #Remove the item from the queue, ie mark as complete

with open(inpFile, "r") as file: #Loads the text file into the 2d maze list
    maze = [[int(i) for i in line.replace(',', '').split()] for line in file]
#https://stackoverflow.com/questions/19201575/python-read-file-look-up-a-string-and-remove-characters user Bartosz Marcinkowski
  
for row, column in enumerate(maze): #Searches for and adds the coordinates of the beginning in (y, x) format
    if 5 in column:
        Queue.append(str(row) + str(column.index(5)))
#https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

try: #Executes all of the movement
    while True:
        move()
except completedPath: #Breaks the loop when exception completedPath is raised (when the maze solver reaches the exit)
    pass

for i in Queue.pop(0).split(): #The 'winning' combination of moves replaces all of the 
    maze[int(i[0])][int(i[1])] = 5

for line in maze: #Prints out the final resultant maze
    print(str(line).strip('[').strip(']').replace(',', ''))