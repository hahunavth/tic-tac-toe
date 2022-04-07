
"""
    empty:  -
    player: x
    player: o
"""

empty = '-'
p1 = 'x'
p2 = 'o'

broad = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]

def isFilled (r, c):
  if broad[c][r] == '-':
    return False
  else:
    return True

def getPlayer(c):
  if c == p1:
    return 1
  elif c == p2:
    return 2
  else:
    return 0

# return 0, 1, 2
def checkWinner():
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
  # Else
  return 0


def fix_spot(row, column, player):
  broad[column][row] = p1 if player == 1 else p2

def print_broad (): 
  for c in range(3):
    print (broad[c])
  print('\n')
