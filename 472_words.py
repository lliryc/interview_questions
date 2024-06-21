from typing import List
from functools import cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Create a prefix tree (trie) to store all words
        prefix_tree = {}
        for word in words:
            node = prefix_tree
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[None] = None  # Mark the end of a word

        @cache
        def can_form(word: str) -> int:
            if word == "":
                return 1  # Base case: an empty word is considered a valid concatenation
            char = word[0]
            if char in prefix_tree:
                return check_subword(word[1:], prefix_tree[char])
            return -1  # Word cannot be formed from the given dictionary

        def check_subword(subword: str, node: dict) -> int:
            if None in node:  # If the current node marks the end of a word
                remaining_check = can_form(subword)
                if remaining_check != -1:
                    return remaining_check + 1  # Increment the count of words forming the concatenation
            if subword == '':
                return -1  # End of the subword reached without forming a valid word
            char = subword[0]
            if char in node:
                return check_subword(subword[1:], node[char])  # Continue checking the next part of the subword
            return -1  # Character not in current prefix tree node

        concatenated_words = set()
        for word in words:
            if can_form(word) > 2:  # A valid concatenated word must be formed by at least two words
                concatenated_words.add(word)

        return list(concatenated_words)  # Convert the set to a list and return

# Example usage
sol = Solution()
print(sol.findAllConcatenatedWordsInADict(words=[
    "cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"
]))

