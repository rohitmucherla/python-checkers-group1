# 0 = empty
# 1 = player 1
# 2 = player 2
# 3 = player 1 king
# 4 = player 2 king
# row 0 is player 1 side
board = [[0 for i in xrange(8)]for z in xrange(8)]  #8x8 array of zeros
pieceX = 0  #x coordinate of piece
pieceY = 0  #y coordinate of piece
player = 1  #1 for player 1 2 for player 2
moveCounter = 0 # number of available moves
moves = [[None] * 2 for y in range(20)]  # Row 0 is the X coordinates of Moves  and Row 1 is the Y Coordinates for Moves

def  moveAbility():
    if player == 1: #player 1 turn
            if board[pieceX][pieceY] == 1: # piece not a king
                    if board[pieceX+1][pieceY+1] == 0: # Top Right Open
                            moves[0][moveCounter]= pieceX + 1
                            moves[1][moveCounter]= pieceY + 1
                            moveCounter = moveCounter + 1
                    if board[pieceX-1][pieceY+1] == 0: # Top Left Open
                        moves[0][moveCounter] = pieceX - 1
                        moves[1][moveCounter] = pieceY + 1
                        moveCounter = moveCounter + 1
                    if board[pieceX+1][pieceY+1] == 2 or board[pieceX+1][pieceY+1] == 4: # Top Right Has Player 2 Piece
                        moves[0][moveCounter] = pieceX + 2
                        moves[1][moveCounter] = pieceY + 2
                        moveCounter = moveCounter + 1
                    if board[pieceX-1][pieceY+1] == 2 or board[pieceX-1][pieceY+1] == 4: # Top Left Has Player 2 Piece
                        moves[0][moveCounter] = pieceX - 2
                        moves[1][moveCounter] = pieceY + 2
                        moveCounter = moveCounter + 1
            else: # piece is a king
                if board[pieceX + 1][pieceY + 1] == 0:  # Top Right Open
                    moves[0][moveCounter] = pieceX + 1
                    moves[1][moveCounter] = pieceY + 1
                    moveCounter = moveCounter + 1
                if board[pieceX - 1][pieceY + 1] == 0:  # Top Left Open
                    moves[0][moveCounter] = pieceX - 1
                    moves[1][moveCounter] = pieceY + 1
                    moveCounter = moveCounter + 1
                if board[pieceX - 1][pieceY - 1] == 0:  # Bot Left Open
                    moves[0][moveCounter] = pieceX - 1
                    moves[1][moveCounter] = pieceY - 1
                    moveCounter = moveCounter + 1
                if board[pieceX + 1][pieceY - 1] == 0:  # Bot Right Open
                    moves[0][moveCounter] = pieceX + 1
                    moves[1][moveCounter] = pieceY - 1
                    moveCounter = moveCounter + 1
                if board[pieceX + 1][pieceY + 1] == 2 or board[pieceX + 1][
                            pieceY + 1] == 4:  # Top Right Has Player 2 Piece
                    moves[0][moveCounter] = pieceX + 2
                    moves[1][moveCounter] = pieceY + 2
                    moveCounter = moveCounter + 1
                if board[pieceX - 1][pieceY + 1] == 2 or board[pieceX - 1][
                            pieceY + 1] == 4:  # Top Left Has Player 2 Piece
                    moves[0][moveCounter] = pieceX - 2
                    moves[1][moveCounter] = pieceY + 2
                    moveCounter = moveCounter + 1
                if board[pieceX + 1][pieceY - 1] == 2 or board[pieceX + 1][
                            pieceY - 1] == 4:  # Bot Right Has Player 2 Piece
                    moves[0][moveCounter] = pieceX + 2
                    moves[1][moveCounter] = pieceY - 2
                    moveCounter = moveCounter + 1
                if board[pieceX - 1][pieceY - 1] == 2 or board[pieceX - 1][
                            pieceY - 1] == 4:  # Bot Left Has Player 2 Piece
                    moves[0][moveCounter] = pieceX - 2
                    moves[1][moveCounter] = pieceY - 2
                    moveCounter = moveCounter + 1

    else: # player 2 turn
        if board[pieceX][pieceY] == 2:  # piece not a king
            if board[pieceX + 1][pieceY - 1] == 0:  # Bot Right Open
                moves[0][moveCounter] = pieceX + 1
                moves[1][moveCounter] = pieceY - 1
                moveCounter = moveCounter + 1
            if board[pieceX - 1][pieceY - 1] == 0:  # Bot Left Open
                moves[0][moveCounter] = pieceX - 1
                moves[1][moveCounter] = pieceY - 1
                moveCounter = moveCounter + 1
            if board[pieceX + 1][pieceY - 1] == 1 or board[pieceX + 1][pieceY - 1] == 3:  # Bot Right Has Player 2 Piece
                moves[0][moveCounter] = pieceX + 2
                moves[1][moveCounter] = pieceY - 2
                moveCounter = moveCounter + 1
            if board[pieceX - 1][pieceY - 1] == 1 or board[pieceX - 1][pieceY - 1] == 3:  # Bot Left Has Player 2 Piece
                moves[0][moveCounter] = pieceX - 2
                moves[1][moveCounter] = pieceY - 2
                moveCounter = moveCounter + 1
        else:  # piece is a king
            if board[pieceX + 1][pieceY + 1] == 0:  # Top Right Open
                moves[0][moveCounter] = pieceX + 1
                moves[1][moveCounter] = pieceY + 1
                moveCounter = moveCounter + 1
            if board[pieceX - 1][pieceY + 1] == 0:  # Top Left Open
                moves[0][moveCounter] = pieceX - 1
                moves[1][moveCounter] = pieceY + 1
                moveCounter = moveCounter + 1
            if board[pieceX - 1][pieceY - 1] == 0:  # Bot Left Open
                moves[0][moveCounter] = pieceX - 1
                moves[1][moveCounter] = pieceY - 1
                moveCounter = moveCounter + 1
            if board[pieceX + 1][pieceY - 1] == 0:  # Bot Right Open
                moves[0][moveCounter] = pieceX + 1
                moves[1][moveCounter] = pieceY - 1
                moveCounter = moveCounter + 1
            if board[pieceX + 1][pieceY + 1] == 1 or board[pieceX + 1][
                        pieceY + 1] == 3:  # Top Right Has Player 2 Piece
                moves[0][moveCounter] = pieceX + 2
                moves[1][moveCounter] = pieceY + 2
                moveCounter = moveCounter + 1
            if board[pieceX - 1][pieceY + 1] == 1 or board[pieceX - 1][
                        pieceY + 1] == 3:  # Top Left Has Player 2 Piece
                moves[0][moveCounter] = pieceX - 2
                moves[1][moveCounter] = pieceY + 2
                moveCounter = moveCounter + 1
            if board[pieceX + 1][pieceY - 1] == 1 or board[pieceX + 1][
                        pieceY - 1] == 1:  # Bot Right Has Player 2 Piece
                moves[0][moveCounter] = pieceX + 2
                moves[1][moveCounter] = pieceY - 2
                moveCounter = moveCounter + 1
            if board[pieceX - 1][pieceY - 1] == 1 or board[pieceX - 1][
                        pieceY - 1] == 3:  # Bot Left Has Player 2 Piece
                moves[0][moveCounter] = pieceX - 2
                moves[1][moveCounter] = pieceY - 2
                moveCounter = moveCounter + 1


def select():
