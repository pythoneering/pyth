# Trying out lists, matrices and a list comprehension.  (Beware - coded on the fly in a pub).
# !! marks points still to learn.
# Incomplete solution to placing 8 queens on a chess board without them attacking one another.

import sys

queens = [ [0] * 8 for i in range(8) ]
# queens = [ [0] * 8 ] * 8    # !! array of 8 refs to the same mutable list: why?


def place_next_queen(column):
  # print("placing", column, queens)
  if queens[7] != [0]*8 :    # all placed
    print_board()
    sys.exit()
  # try all squares that aren't attacked on that row, upward diagonal or downward diagonal
  for row in range(8) :
    if safe(column,row) :
      print("is safe ", column, row)
      queens[column][row]=1
      place_next_queen(column+1)
      print("no soln ", column, row)
      queens[column][row]=0
  return    # backtrack

def safe(column,row):
  # print("safe? ", column, row)
  # need to check diagonals as well, this only checks rows
  this_row_attacked = [ True for col in queens if col[row] != 0 ]    # for the sake of it :)
  return this_row_attacked == []

  #  attacked = zip(queens)    # !! couldn't get zip object to work
  #  return attacked[row] != [0] * 8

def print_board():
  print("board is ", queens)

# queens[1][3]=1    # force failure for testing
place_next_queen(0)    # has to be defined prior to invocation: !! seems clunky
# if we're here PNQ has terminated so it's found a solution
