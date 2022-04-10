# """
# Rule in Tic -Tac –Toe
#   Rule 1 If the player has a winning move, take it.
#   Rule 2 If the opponent has a winning move, block it.
#   Rule 3 If the player can create a fork (two winning
#   ways) after this move, take it.
#   Rule 4 Do not let the opponent create a fork after the
#   player’s move.
#   Rule 5 Move in a way such as the player may win the
#   most number of possible ways. 
# """

# """
# Flow:
# function findBestMove(board):
#     bestMove = NULL
#     for each move in board :
#         if current move is better than bestMove
#             bestMove = current move
#     return bestMove
# """

# from constants import player, opponent, empty
 
# # This function returns true if there are moves
# # remaining on the board. It returns false if
# # there are no moves left to play.
# def isMovesLeft(board) :
 
#     for i in range(3) :
#         for j in range(3) :
#             if (board[i][j] == empty) :
#                 return True
#     return False
 
# # This is the evaluation function as discussed
# def evaluate(b) :
   
#     # Checking for Rows for X or O victory.
#     for row in range(3) :    
#         if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
#             if (b[row][0] == player) :
#                 return 10
#             elif (b[row][0] == opponent) :
#                 return -10
 
#     # Checking for Columns for X or O victory.
#     for col in range(3) :
      
#         if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
#             if (b[0][col] == player) :
#                 return 10
#             elif (b[0][col] == opponent) :
#                 return -10
 
#     # Checking for Diagonals for X or O victory.
#     if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
#         if (b[0][0] == player) :
#             return 10
#         elif (b[0][0] == opponent) :
#             return -10
 
#     if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
#         if (b[0][2] == player) :
#             return 10
#         elif (b[0][2] == opponent) :
#             return -10
 
#     # Else if none of them have won then return 0
#     return 0
 
# # This is the minimax function. It considers all
# # the possible ways the game can go and returns
# # the value of the board
# def minimax(board, depth, isMax) :
#     score = evaluate(board)
 
#     # If Maximizer has won the game return his/her
#     # evaluated score
#     if (score == 10) :
#         return score
 
#     # If Minimizer has won the game return his/her
#     # evaluated score
#     if (score == -10) :
#         return score
 
#     # If there are no more moves and no winner then
#     # it is a tie
#     if (isMovesLeft(board) == False) :
#         return 0
 
#     # If this maximizer's move
#     if (isMax) :    
#         best = -1000
 
#         # Traverse all cells
#         for i in range(3) :        
#             for j in range(3) :
              
#                 # Check if cell is empty
#                 if (board[i][j]==empty) :
                 
#                     # Make the move
#                     board[i][j] = player
 
#                     # Call minimax recursively and choose
#                     # the maximum value
#                     best = max( best, minimax(board,
#                                               depth + 1,
#                                               not isMax) )
 
#                     # Undo the move
#                     board[i][j] = empty
#         return best
 
#     # If this minimizer's move
#     else :
#         best = 1000
 
#         # Traverse all cells
#         for i in range(3) :        
#             for j in range(3) :
              
#                 # Check if cell is empty
#                 if (board[i][j] == empty) :
                 
#                     # Make the move
#                     board[i][j] = opponent
 
#                     # Call minimax recursively and choose
#                     # the minimum value
#                     best = min(best, minimax(board, depth + 1, not isMax))
 
#                     # Undo the move
#                     board[i][j] = empty
#         return best
 
# # This will return the best possible move for the player
# def findBestMove(board) :
#     bestVal = -1000
#     bestMove = (-1, -1)
 
#     # Traverse all cells, evaluate minimax function for
#     # all empty cells. And return the cell with optimal
#     # value.
#     for i in range(3) :    
#         for j in range(3) :
         
#             # Check if cell is empty
#             if (board[i][j] == empty) :
             
#                 # Make the move
#                 board[i][j] = player
 
#                 # compute evaluation function for this
#                 # move.
#                 moveVal = minimax(board, 0, False)
 
#                 # Undo the move
#                 board[i][j] = empty
 
#                 # If the value of the current move is
#                 # more than the best value, then update
#                 # best/
#                 if (moveVal > bestVal) :               
#                     bestMove = (i, j)
#                     bestVal = moveVal
 
#     print("The value of the best Move is :", bestVal)
#     print()
#     return bestMove

# ------------------------------------

from constants import empty
from logic import getPlayer

def print_broad (b): 
  for c in range(3):
    print (b[c])

def checkWinner(broad):
  # Cross
  if broad[0][0] == broad[1][1] and broad[1][1] == broad[2][2] and broad[0][0] != empty:
    return getPlayer(broad[0][0])
  if broad[0][2] == broad[1][1] and broad[1][1] == broad[2][0] and broad[1][1] != empty:
    return getPlayer(broad[1][1])
  # Row or column
  for i in range(len(broad)):
    if broad[i][0] == broad[i][1] and broad[i][1] == broad[i][2] and broad[i][0] != empty:
      return getPlayer(broad[i][0])
    elif broad[0][i] == broad[1][i] and broad[1][i] == broad[2][i] and broad[0][i] != empty:
      return getPlayer(broad[0][i])

  # Tier
  isTier = True
  for r in range(3):
    for c in range(3):
        if broad[r][c] == '-':
            isTier = False

  # Else
  if isTier:
    return 0
  else:
   return None

def minimax (broad, depth=0, isMaxizing=True):
    w = checkWinner(broad)
    # print_broad(broad)
    # print(w)
    if w == 2:
        return -10
    if w == 1:
        return 10
    if w == 0:
        return 0

    if isMaxizing:
        best_score = -1000000
        for r in range(3):
            for c in range(3):
                if(broad[r][c] == '-'):
                    broad[r][c] = 'x'
                    score = minimax(broad, depth + 1, False)
                    best_score = max(best_score, score) * 0.9
                    broad[r][c] = '-'
        return best_score
    
    else:
        best_score = 1000000
        for r in range(3):
            for c in range(3):
                if(broad[r][c] == '-'):
                    broad[r][c] = 'o'
                    score = minimax(broad, depth + 1, True)
                    # print(f'{score} < {best_score}')
                    best_score = min(best_score, score) * 1.1
                    broad[r][c] = '-'
        return best_score


def findBestMove (broad):
    best_score = - 1000000
    best_move = None
    for r in range(3):
        for c in range(3):
            # print("Loop!-------------------")
            if(broad[r][c] == '-'):
                broad[r][c] = 'x'
                score = minimax(broad, 0, False)
                # print(score)
                if(score > best_score):
                    best_score = score
                    best_move = (r,c)
                broad[r][c] = '-'
    return best_move



# Driver code
if __name__ == '__main__':
  board = [
      [ 'x', 'o', 'x' ],
      [ 'o', 'o', 'x' ],
      [ '-', '-', '-' ]
  ]
  bestMove = findBestMove(board)
  print(f'The Optimal Move is : {bestMove}' )
  
#   bestMove = findBestMove(board)
  
#   print("ROW:", bestMove[0], " COL:", bestMove[1])
 

