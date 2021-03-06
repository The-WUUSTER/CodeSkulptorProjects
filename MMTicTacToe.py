"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import random

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    winner = board.check_win()
    if winner != None:
        return SCORES[winner], (-1, -1)
        
    empty_squares = board.get_empty_squares()
    if len(empty_squares) == board.get_dim() ** 2:
        ideal_starting_squares = [(0,0), (0,board.get_dim()-1), (board.get_dim()-1, 0), (board.get_dim()-1, board.get_dim()-1)]
        return SCORES[player], random.choice(ideal_starting_squares)
        
    best_move = (-1, -1)
    best_score = float("-inf")
    for square in empty_squares:
        clone = board.clone()
        clone.move(square[0], square[1], player)
        clone_move = mm_move(clone, provided.switch_player(player))
        score = SCORES[player] * clone_move[0]
        if score == 1:
            return clone_move[0], square
        elif score == 0:
            best_score = 0
            best_move = square
        if score > best_score:
            best_score = clone_move[0]
            best_move = square
    return best_score, best_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


# Test game with the console or the GUI.
# Uncomment whichever you prefer.

#provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
