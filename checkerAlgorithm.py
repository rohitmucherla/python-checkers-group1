# 0 = empty
# 1 = player 1
# 2 = player 1 king
# 3 = player 2
# 4 = player 2 king
# row 0 is player 1 side
board = [[0 for i in xrange(8)]for z in xrange(8)]  #8x8 array of zeros
pieceX = 0  #x coordinate of piece
pieceY = 0  #y coordinate of piece
player = 1  #1 for player 1 2 for player 2

def  moveAbility():
    moves = [[None]*2 for y in range(20)] # 2x20 array for possible moves
    if player == 1: #player 1 turn
        {
            if board[pieceX][pieceY] == 1: # piece not a king
                {
                    if board[pieceX+1][pieceY+1] == 0: # Top Right Open
                        {
                            for row in range()
                           moves[0][0]
                        }
                    if board[pieceX-1][pieceY+1] == 0: # Top Left Open
                        {

                        }

                }
            else: # piece is a king
                {

                }

        }
    else: # player 2 turn
        {

        }

