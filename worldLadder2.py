from typing import List, Dict
from collections import defaultdict

class Solution:
    """
    A class to solve the Word Ladder problem.

    The Word Ladder problem is to find the shortest transformation sequence
    from a begin word to an end word, changing only one letter at a time,
    and each intermediate word must exist in the given word list.

    Attributes:
        min_path_len (int): The length of the shortest path found.
        min_paths (List[List[str]]): List of all shortest paths found.
        graph (Dict[str, List[str]]): Graph representation of word connections.
        end_word (str): The target word to reach.
    """

    def __init__(self):
        self.min_path_len = float('inf')
        self.min_paths = []
        self.graph = defaultdict(list)
        self.end_word = ""

    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        """
        Find all shortest transformation sequences from begin_word to end_word.

        Args:
            begin_word (str): The starting word.
            end_word (str): The target word.
            word_list (List[str]): List of valid intermediate words.

        Returns:
            List[List[str]]: All shortest transformation sequences.
        """
        # Reset instance variables
        self.min_path_len = float('inf')
        self.min_paths = []
        self.graph = defaultdict(list)
        self.end_word = end_word

        # Create a set of words for faster lookup
        word_set = set(word_list)
        word_set.add(begin_word)

        # Build the graph and sort neighbors
        self._build_graph(word_set)
        self._sort_graph_neighbors(end_word)

        # Perform BFS to find shortest paths
        self._bfs(begin_word)

        return self.min_paths

    def _build_graph(self, word_set: set):
        """
        Build a graph where words are connected if they differ by one letter.

        Args:
            word_set (set): Set of all words to consider.
        """
        for word in word_set:
            for i in range(len(word)):
                # Create a generic pattern by replacing each character with '*'
                pattern = word[:i] + '*' + word[i+1:]
                for neighbor in word_set:
                    if neighbor != word and self._is_neighbor(word, neighbor):
                        self.graph[word].append(neighbor)

    def _sort_graph_neighbors(self, end_word: str):
        """
        Sort neighbors of each word based on their similarity to the end word.

        Args:
            end_word (str): The target word to reach.
        """
        for word in self.graph:
            self.graph[word].sort(key=lambda x: self._word_difference(x, end_word))

    def _is_neighbor(self, word1: str, word2: str) -> bool:
        """
        Check if two words are neighbors (differ by exactly one letter).

        Args:
            word1 (str): First word.
            word2 (str): Second word.

        Returns:
            bool: True if words are neighbors, False otherwise.
        """
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

    def _word_difference(self, word1: str, word2: str) -> int:
        """
        Calculate the number of different characters between two words.

        Args:
            word1 (str): First word.
            word2 (str): Second word.

        Returns:
            int: Number of characters that differ between the words.
        """
        return sum(c1 != c2 for c1, c2 in zip(word1, word2))

    def _bfs(self, start: str):
        """
        Perform Breadth-First Search to find all shortest paths.

        Args:
            start (str): The starting word.
        """
        queue = [[start]]
        visited = {start: 0}

        while queue:
            path = queue.pop(0)
            word = path[-1]

            # If current path is longer than the shortest found, stop searching
            if len(path) > self.min_path_len:
                break

            if word == self.end_word:
                if len(path) < self.min_path_len:
                    # Found a shorter path
                    self.min_paths = [path]
                    self.min_path_len = len(path)
                elif len(path) == self.min_path_len:
                    # Found another path of the same length
                    self.min_paths.append(path)
                continue

            for neighbor in self.graph[word]:
                if neighbor not in visited or visited[neighbor] >= len(path) + 1:
                    queue.append(path + [neighbor])
                    visited[neighbor] = len(path)

import unittest

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        """
        Set up a Solution instance before each test.
        """
        self.solution = Solution()

    def test_findLadders_example1(self):
        """
        Test the findLadders method with a standard example.
        """
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
        result = self.solution.findLadders(begin_word, end_word, word_list)
        self.assertEqual(sorted(result), sorted(expected))

    def test_findLadders_no_solution(self):
        """
        Test the findLadders method when there's no solution.
        """
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log"]
        expected = []
        result = self.solution.findLadders(begin_word, end_word, word_list)
        self.assertEqual(result, expected)

    def test_findLadders_single_step(self):
        """
        Test the findLadders method with a single-step transformation.
        """
        begin_word = "dog"
        end_word = "cog"
        word_list = ["cog"]
        expected = [["dog", "cog"]]
        result = self.solution.findLadders(begin_word, end_word, word_list)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
