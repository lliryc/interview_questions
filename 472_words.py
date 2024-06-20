from typing import List
from functools import cache
from collections import defaultdict

class Solution:

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        prefixd = {}
        for w in words:
            d = prefixd
            for c in w:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d[None] = None

        @cache
        def check(word):
            if word == "":
                return 1
            c = word[0]
            if c in prefixd:
                return check2(word[1:], prefixd[c])
            else:
                return -1

        def check2(word, d):
            if None in d:
                r = check(word)
                if r != -1:
                    return r + 1
            if word == '':
                return -1
            c = word[0]
            if c in d:
                return check2(word[1:], d[c])
            return -1

        outputs = set([])
        for w in words:
            if check(w) > 2:
                outputs.add(w)

        return list(outputs)

sol = Solution()
print(sol.findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))

