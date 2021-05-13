import pygame, sys
import random

# Number of frames per second
def initiateVals(SIZE):
    global FPS, WINDOWMULTIPLIER, WINDOWSIZE, WINDOWWIDTH, WINDOWHEIGHT
    global SQUARESIZE, CELLSIZE, NUMBERSIZE
    global BLACK, WHITE, LIGHTGRAY, BLUE, PURPLE
    FPS = 10
    # SIZE = int(input("Enter in 3 for a 9x9 grid or a 2 for a 4x4 grid "))
    # Sets size of grid
    WINDOWMULTIPLIER = 5  # Modify this number to change size of grid
    WINDOWSIZE = 81
    WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
    WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
    SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / SIZE)  # size of a 3x3 square
    CELLSIZE = int(SQUARESIZE / SIZE)  # Size of a cell
    NUMBERSIZE = int(CELLSIZE / SIZE)  # Position of unsolved number

    # Set up the colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    LIGHTGRAY = (200, 200, 200)
    BLUE = (0, 0, 255)
    PURPLE = (148, 96, 224)


def drawGrid():
    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0, y), (WINDOWWIDTH, y))

    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, SQUARESIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))

    return None
def generateGrid(size):
    gridnum = random.randint(1, 2)
    if size == 3:
        if gridnum == 1:
            grid = dict(
                [((0, 0), 5), ((0, 1), 3), ((0, 4), 7), ((1, 0), 6), ((1, 3), 1), ((1, 4), 9), ((1, 5), 5), ((3, 1), 9),
                 ((3, 2), 8), ((3, 7), 6), ((4, 1), 8), ((4, 4), 6), ((4, 8), 3), ((5, 1), 4), ((5, 3), 2), ((5, 8), 6),
                 ((6, 1), 6), ((6, 6), 2), ((6, 7), 8), ((7, 3), 4), ((7, 4), 1), ((7, 5), 9), ((7, 8), 5), ((8, 4), 8),
                 ((8, 7), 7), ((8, 8), 9)])
            #grid = dict([((0,0), 5), ((0,1), 6), ((1,0),3), ((2,1),9), ((2,2),8)])
        else:
            #grid = dict([((0, 0), 5), ((0, 1), 1)])
            grid = dict(
                [((0, 0), 1), ((0, 1), 4), ((0, 3), 2), ((0, 8), 7), ((1, 7), 6), ((2, 3), 7), ((2, 5), 1), ((2, 7), 3),
                 ((3, 7), 1), ((4, 0), 4), ((4, 1), 8), ((4, 2), 7), ((4, 6), 5), ((5, 3), 8), ((5, 4), 4), ((5, 5), 5),
                 ((6, 2), 9), ((6, 6), 3), ((7, 1), 3), ((7, 3), 6), ((7, 4), 8), ((7, 5), 2), ((8, 1), 6), ((8, 1), 6),
                 ((8, 5), 4)])
    elif size == 2:
        if gridnum == 1:
            #grid = dict([((0, 0), 1)])
            grid = dict([((0, 0), 3), ((0, 4), 2), ((1, 1), 1), ((1, 2), 4), ((0, 2), 4), ((2, 3), 1), ((3, 1), 2),
                          ((3, 2), 3)])
        else:
            grid = dict([((0, 0), 2)])
    return grid


def initiateCells(size):
    currentGrid = {}
    if size == 3:
        fullcell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        grid = generateGrid(size)
    else:
        fullcell = [1, 2, 3, 4]
        grid =  generateGrid(size)
    for xCoord in range(0, size * size):
        for yCoord in range(0, size * size):
            currentGrid[xCoord, yCoord] = list(fullcell)
    #grid = dict([((0,0), 5), ((0,1), 6), ((1,0),3), ((2,1),9), ((2,2),8)])
    for k, v in grid.items():
        incNum = 0
        xCellNumber = k[0]
        yCellNumber = k[1]
        number = v

        currentState = currentGrid[xCellNumber, yCellNumber]
        while incNum < (size * size):
            # if NOT number selected
            if incNum + 1 != number:
                currentState[incNum] = ' '  # make ' '
            else:
                currentState[incNum] = number  # make = number
        # update currentGrid
            currentGrid[xCellNumber, yCellNumber] = currentState
            incNum += 1

    print(currentGrid)
    return currentGrid


def displayCells(currentGrid, size):
    # Create offset factors to display numbers in right location in cells.
    xFactor = 0
    yFactor = 0
    for item in currentGrid:  # item is x,y co-ordinate from 0 -8
        cellData = currentGrid[item]  # isolates the numbers still available for that cell
        for number in cellData:  # iterates through each number
            if number != ' ':  # ignores those already dismissed
                xFactor = ((number - 1) % size)  # 1/4/7 = 0 2/5/8 = 1 3/6/9 =2
                if size == 3:
                    if number <= 3:
                        yFactor = 0
                    elif number <= 6:
                        yFactor = 1
                    else:
                        yFactor = 2
                else:
                    if number <= 2:
                        yFactor = 0
                    else:
                        yFactor = 1
            if size == 3:
                if cellData.count(' ') < 8:
                    populateCells(number, (item[0] * CELLSIZE) + (xFactor * NUMBERSIZE),
                                  (item[1] * CELLSIZE) + (yFactor * NUMBERSIZE), 'small')
                else:
                    populateCells(number, (item[0] * CELLSIZE), (item[1] * CELLSIZE), 'large')
            else:
                if cellData.count(' ') < 3:
                    populateCells(number, (item[0] * CELLSIZE) + (xFactor * NUMBERSIZE),
                                  (item[1] * CELLSIZE) + (yFactor * NUMBERSIZE), 'small')
                else:
                    populateCells(number, (item[0] * CELLSIZE), (item[1] * CELLSIZE), 'large')
    return None


# writes cellData at given x, y co-ordinates
def populateCells(cellData, x, y, numberfontsize):
    if numberfontsize == 'small':
        cellSurf = BASICFONT.render('%s' % (cellData), True, LIGHTGRAY)
    elif numberfontsize == 'large':
        cellSurf = LARGEFONT.render('%s' % (cellData), True, PURPLE)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)


def drawBox(mousex, mousey, size):
    boxx = ((mousex * (size * size * size)) / WINDOWWIDTH) * (NUMBERSIZE)  # 27 number of squares
    boxy = ((mousey * (size * size * size)) / WINDOWHEIGHT) * (NUMBERSIZE)  # 27 number of squares
    pygame.draw.rect(DISPLAYSURF, BLUE, (boxx, boxy, NUMBERSIZE, NUMBERSIZE), 1)


def displaySelectedNumber(mousex, mousey, currentGrid, size):
    xNumber = (mousex * (size * size * size)) / WINDOWWIDTH  # xNumber in range 0 - 26
    yNumber = (mousey * (size * size * size)) / WINDOWWIDTH  # yNumber in range 0 - 26
    # Determine a 0,1 or 2 for x and y
    modXNumber = int(xNumber % size)
    modYNumber = int(yNumber % size)
    if size == 3:
        if modXNumber == 0:
            xChoices = [1, 4, 7]
            number = xChoices[modYNumber]
        elif modXNumber == 1:
            xChoices = [2, 5, 8]
            number = xChoices[modYNumber]
        else:
            xChoices = [3, 6, 9]
            number = xChoices[modYNumber]
    else:
        if modXNumber == 0:
            xChoices = [1, 3]
            number = xChoices[modYNumber]
        else:
            xChoices = [2, 4]
            number = xChoices[modYNumber]
    # need to determine the cell we are in
    xCellNumber = int(xNumber / size)
    yCellNumber = int(yNumber / size)

    # gets a list of current numbers
    currentState = currentGrid[xCellNumber, yCellNumber]
    incNum = 0

    while incNum < (size * size):
        # if NOT number selected
        if incNum + 1 != number:
            currentState[incNum] = ' '  # make ' '
        else:
            currentState[incNum] = number  # make = number
        # update currentGrid
        currentGrid[xCellNumber, yCellNumber] = currentState
        incNum += 1

    solveSudoku(currentGrid, size)

    return currentGrid


def solveSudoku(currentGrid, size):
    for item in currentGrid:  # item is x,y co-ordinate from 0-8
        cellData = currentGrid[item]  # isolates the numbers still available for that cell
        if cellData.count(' ') == (size * size) - 1:  # only look at those with one number remaining
            for number in cellData:  # Determine the number there
                if number != ' ':
                    updateNumber = number

            currentGrid = removeX(currentGrid, item, updateNumber, size)
            currentGrid = removeY(currentGrid, item, updateNumber, size)
            currentGrid = removeGrid(currentGrid, item, updateNumber, size)

    return currentGrid


def removeX(currentGrid, item, number, size):
    for x in range(0, size):
        if x != item[0]:
            currentState = currentGrid[(x, item[1])]
            currentState[number - 1] = ' '
            currentGrid[(x, item[1])] = currentState
    return currentGrid


def removeY(currentGrid, item, number, size):
    for y in range(0, size):
        if y != item[1]:
            currentState = currentGrid[(item[0], y)]
            currentState[number - 1] = ' '
            currentGrid[(item[0], y)] = currentState
    return currentGrid


def removeGrid(currentGrid, item, number, size):
    if size == 3:
        if item[0] < 3:
            xGrid = [0, 1, 2]
        elif item[0] > 5:
            xGrid = [6, 7, 8]
        else:
            xGrid = [3, 4, 5]

        if item[1] < 3:
            yGrid = [0, 1, 2]
        elif item[1] > 5:
            yGrid = [6, 7, 8]
        else:
            yGrid = [3, 4, 5]
    else:
        if item[0] < 2:
            xGrid = [0, 2]
        else:
            xGrid = [1, 3]

        if item[1] < 2:
            yGrid = [0, 2]
        else:
            yGrid = [1, 3]

    # iterates through each of the nine numbers in the grid
    for x in xGrid:
        for y in yGrid:
            if (x, y) != item:  # for all squares except the one containing the number
                currentState = currentGrid[(x, y)]  # isolates the numbers still available for that cell
                currentState[number - 1] = ' '  # make them blank.
                currentGrid[(x, y)] = currentState

    return currentGrid


def sudoku(SIZE):
    initiateVals(SIZE)
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Sudoku Game')

    mouseClicked = False
    mousex = 0
    mousey = 0

    global BASICFONT, BASICFONTSIZE, LARGEFONT, LARGEFONTSIZE
    BASICFONTSIZE = 15
    LARGEFONTSIZE = 55
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)
    DISPLAYSURF.fill(WHITE)

    # Selecting grid size based off user input in the function
    currentGrid = initiateCells(SIZE)
    displayCells(currentGrid, SIZE)

    drawGrid()
    # repaints screen
    DISPLAYSURF.fill(WHITE)
    displayCells(currentGrid, SIZE)
    drawGrid()
    while True:  # main game loop
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            # Mouse click commands
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        if mouseClicked == True:
            # allow number to be selected
            currentGrid = displaySelectedNumber(mousex, mousey, currentGrid, SIZE)
        solveSudoku(currentGrid, SIZE)
        # repaints screen
        DISPLAYSURF.fill(WHITE)
        displayCells(currentGrid, SIZE)
        drawGrid()
        # call function to draw box
        drawBox(mousex, mousey, SIZE)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
