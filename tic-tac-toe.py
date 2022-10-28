import random
def displayBoard(b):
    print(b[1]+'|'+b[2]+'|'+b[3])
    print(b[4]+'|'+b[5]+'|'+b[6])
    print(b[7]+'|'+b[8]+'|'+b[9])
def isWinner(b,p):
    return (((b[1]==p)and(b[2]==p)and(b[3]==p))or
            ((b[4]==p)and(b[5]==p)and(b[6]==p))or
            ((b[7]==p)and(b[8]==p)and(b[9]==p))or
            ((b[1]==p)and(b[4]==p)and(b[7]==p))or
            ((b[2]==p)and(b[5]==p)and(b[8]==p))or
            ((b[3]==p)and(b[6]==p)and(b[9]==p))or
            ((b[1]==p)and(b[5]==p)and(b[9]==p))or
            ((b[3]==p)and(b[5]==p)and(b[7]==p)))
def whoGoesFirst():
    if(random.randint(0,1)==0):
        return 'computer'
    else:
        return 'player'
def inputPlayerLetter():
    print("Do you want X or O")
    i=input().lower()
    if(i=='x'):
        return ['X','O']
    else:
        return ['O','X']
def PlayAgain():
    print("do you want to play again?")
    return(input().lower().startswith('y'))
def makeMove(board,letter,position):
    board[position]=letter
def getBoardCopy(board):
    dup=[]
    for i in board:
        dup.append(i)
    return dup
def isSpaceFree(board,position):
    return board[position]==''
def getPlayerMove(board):
    move=''
    while((move not in '1 2 3 4 5 6 7 8 9'.split())or(not isSpaceFree(board,int(move)))):
        move=input("Enter your move")
    return int(move)
def chososeRandomMoveFromList(board,moveList):
    possible=[]
    for i in moveList:
        if(isSpaceFree(board,i)):
            possible.append(i)
    if(len(possible)!=0):
        return random.choice(possible)
    else:
        return None
def getComputerMove(board,cL,pL):
    for i in range(1,10):
        dup=getBoardCopy(board)
        if(isSpaceFree(dup,i)):
            makeMove(dup,cL,i)
            if(isWinner(dup,cL)):
                return i
    for i in range(1,10):
        dup=getBoardCopy(board)
        if(isSpaceFree(dup,i)):
            makeMove(dup,pL,i)
            if(isWinner(dup,pL)):
                return i
    move=chososeRandomMoveFromList(board,[1,3,7,9])
    if (move!=None):
        return move
    elif(isSpaceFree(board,5)):
        return 5
    else:
        return chososeRandomMoveFromList(board,[2,4,6,8])
def isFull(board):
    for i in range(1,10):
        if(isSpaceFree(board,i)):
            return False
    return True
print("Play Tic Tac Toe")
playAgain=True
while True:
    board=['']*10
    pL,cL=inputPlayerLetter()
    turn=whoGoesFirst()
    print(turn+" goes First")
    while playAgain:
        if(turn=='player'):
            displayBoard(board)
            move=getPlayerMove(board)
            makeMove(board,pL,move)
            if(isWinner(board,pL)):
                displayBoard(board)
                print("Player Won")
                playAgain=False
            elif(isFull(board)):
                displayBoard(board)
                print("Its a tie")
                break
            else:
                turn='computer'
        elif(turn=='computer'):
            displayBoard(board)
            move=getComputerMove(board,cL,pL)
            makeMove(board,cL,move)
            if(isWinner(board,cL)):
                displayBoard(board)
                print("Computer Won")
                playAgain=False
            elif(isFull(board)):
                displayBoard(board)
                print("Its a tie")
                break
            else:
                turn='player'
    playAgain=PlayAgain()