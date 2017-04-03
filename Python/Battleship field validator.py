def validateBattlefield(field):
    rows, cols = 10, 10
    checked = []
    for row in range(rows):
        checked.append([])
        for col in range(cols):
            checked[row].append(False)
    ships = []
    
    def inRange(row,col):
        return row>=0 and row<rows and col>=0 and col<cols
    def check(row,col):
        if not checked[row][col]:
            if field[row][col]==1:
                ships.append(ship(row,col))
        checked[row][col]=True
    def ship(row,col):
        components=[]
        components.append([row,col])
        #check rows
        vertical=False
        newRow = row+1
        while inRange(newRow,col):
            if not checked[newRow][col]:
                checked[newRow][col]=True
                if field[newRow][col]==1:
                    vertical=True
                    components.append([newRow,col])
                else:
                    break
            else:
                break
            newRow+=1
        #check cols
        newCol=col+1
        if not vertical:
            while inRange(row,newCol):
                if not checked[row][newCol]:
                    checked[row][newCol]=True
                    if field[row][newCol]==1:
                        components.append([row,newCol])
                    else:
                        break
                else:
                    break
                newCol+=1
        return components
    
    for row in range(rows):
        for col in range(cols):
            check(row,col)
    battleships, cruisers, destroyers, submarines = 0,0,0,0
    for ship in ships:
        if len(ship)==1:
            submarines+=1
        elif len(ship)==2:
            destroyers+=1
        elif len(ship)==3:
            cruisers+=1
        elif len(ship)==4:
            battleships+=1
        else:
            return False
        for component in ship:
            row,col=component[0],component[1]
            for x in range(row-1,row+2):
                for y in range(col-1,col+2):
                    if inRange(x,y):
                        if field[x][y]==1 and not [x,y] in ship:
                            return False
    if not (battleships==1 and cruisers==2 and destroyers==3 and submarines==4):
        return False
    return True
	
	"""
	Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:

    There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.

    Each ship must be a straight line, except for submarines, which are just single cell.

    The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
"""
