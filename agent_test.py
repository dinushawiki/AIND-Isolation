"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

class IsolationTest(unittest.TestCase):

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        
    def test_heuristic(self):
        """ Test output interface of heuristic score function interface."""

        player1 = "Player1"
        player2 = "Player2"
        p1_location = (2, 1)
        p2_location = (1, 1)  # top left corner
        game = isolation.Board(player1, player2)
        game.apply_move(p1_location)
        game.apply_move(p2_location)
        
        player_1_moves = game.get_legal_moves(player1)
        player_2_moves = game.get_legal_moves(player2)
        print(game.to_string())
        print(player_1_moves)
        print(player_2_moves)
        print(game_agent.custom_score(game, player1))

        self.assertIsInstance(game_agent.custom_score(game, player1), float,
            "The heuristic function should return a floating point")
    def test_minimax_interface(self):
        
        h, w = 7, 7  # board size
        search_depth = 2
        p1_location = (2, 1)
        p2_location = (1, 1)  # top left corner
        
      
        # create a player agent & a game board
        agentUT = game_agent.MinimaxPlayer(
            search_depth)
        agentUT.time_left = lambda: 99  # ignore timeout for fixed-depth search
        board = isolation.Board(agentUT, 'null_agent', w, h)
                
        # place two "players" on the board at arbitrary (but fixed) locations
        board.apply_move(p1_location)
        board.apply_move(p2_location)

        
        best_move = agentUT.get_move(board,time_left=lambda: 99)
        print(best_move)

    def test_alphabeta_interface(self):
        """ Test CustomPlayer.alphabeta interface with simple input """
        h, w = 9, 9  # board size
        search_depth = 2
        starting_location = (2, 1)
        adversary_location = (1, 1)  # top left corner
        
        # create a player agent & a game board
        agentUT = game_agent.AlphaBetaPlayer(
            search_depth)
        agentUT.time_left = lambda: 99  # ignore timeout for fixed-depth search
        board = isolation.Board(agentUT, 'null_agent', w, h)
        
        # place two "players" on the board at arbitrary (but fixed) locations
        board.apply_move(starting_location)
        board.apply_move(adversary_location)
        print(board.to_string())
        
        best_move = agentUT.get_move(board,time_left=lambda: 99)
        print(best_move)


if __name__ == '__main__':
    unittest.main()
