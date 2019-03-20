import numpy as np
import time

player1 = np.array([[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]])
player2 = np.array([[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]])
'''
test0 = np.array([[0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1]])

test1 = np.array([[1,1,1,1,1],
             [1,1,1,1,1],
             [1,1,1,1,1],
             [1,1,1,1,1],
             [1,1,1,1,1]])

#winner = False
#gameMode = Standard or Full
'''
#victory conditions
def victoryChecker(gameBoard):
    if np.sum(gameBoard) == 25:
        return "DOMINATION VICTORY"
    elif gameBoard[0][0] + gameBoard[1][1] + gameBoard[2][2] + gameBoard[3][3] + gameBoard[4][4] == 5:
        print("RIGHT DIAGONAL VICTORY")
    elif gameBoard[0][4] + gameBoard[1][3] + gameBoard[2][2] + gameBoard[3][1] + gameBoard[4][0] == 5:
        print("LEFT DIAGONAL VICTORY")
    elif np.sum(gameBoard[0]) == 5:
        print("FIRST ROW VICTORY")
    elif np.sum(gameBoard[1]) == 5:
        print("SECOND ROW VICTORY")
    elif np.sum(gameBoard[2]) == 5:
        print("THIRD ROW VICTORY")
    elif np.sum(gameBoard[3]) == 5:
        print("FOURTH ROW VICTORY")
    elif np.sum(gameBoard[4]) == 5:
        print("FIFTH ROW VICTORY")
    elif np.sum(gameBoard[:,0]) == 5:
        print("FIRST COL VICTORY")
    elif np.sum(gameBoard[:,1]) == 5:
        print("SECOND COL VICTORY")
    elif np.sum(gameBoard[:,2]) == 5:
        print("THIRD COL VICTORY")
    elif np.sum(gameBoard[:,3]) == 5:
        print("FOURTH COL VICTORY")
    elif np.sum(gameBoard[:,4]) == 5:
        print("FIFTH COL VICTORY")
    else:
        return "NO VICTORY"


def victoryFull(gameBoard):
    if np.sum(gameBoard) == 25:
        print("DOMINATION VICTORY")
    

'''
def fourCorners(gameBoard):
    if gameBoard[0,0] + gameBoard[0][4] + gameBoard[4][0] + gameBoard[4][4] == 4:
        print("FOUR CORNERS VICTORY")
    else:
        print("NO VICTORY")
'''

#victoryFull(test0)
#victoryChecker(test1)

start = time.time()
product = victoryChecker(player1)
elapsed = (time.time() - start)

print ("result %s returned in %s seconds." % (product,elapsed))