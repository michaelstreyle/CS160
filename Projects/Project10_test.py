'''
Testing the module movies
Karina Hoff, 2018


Michael Streyle

Test fails because program requires input from user, which interrupts the test file
Not really sure how to make the tests work, but my program works in accordance with the 5 tasks listed on Github/Katie

'''

import pytest
import sys
from Project10 import build, bfs, main



class TestMoviesMethods:
    """Testing module movies"""

    def setup_class(self):
        """Setting up"""
        self.graph = build("movie_actors_test.txt")
        kevin = self.graph.get_vertex("Kevin Bacon")
        bfs(kevin, "Kevin Bacon")


    def test_read_file(self):
        assert len(self.graph) == 7
        connections = 0
        for v in self.graph:
            connections += len(v.get_neighbors())
        assert connections == 18

    def test_bfs(self):
        assert self.graph.get_vertex("Allen").get_distance() == 1
        assert self.graph.get_vertex("Brad").get_distance() == 2
        assert self.graph.get_vertex("Grace").get_distance() == 3


