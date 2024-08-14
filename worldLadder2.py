from typing import List, Dict
from collections import defaultdict

class Solution:

    def __init__(self):
        self.min_path_len = 2**32
        self.min_path = []
        self.graph = defaultdict(List)
        self.visited = {}
        self.endWord = ""

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.min_path_len = 2**32
        self.graph = defaultdict(list)
        self.visited = {}
        self.endWord = endWord
        wordList = list(set(wordList))
        wordList.append(beginWord)
        for i in range(len(wordList) - 1):
            for j in range(i+1, len(wordList)):
                if self.diff(wordList[i],wordList[j]) == 1:
                    self.graph[wordList[i]].append(wordList[j])
                    self.graph[wordList[j]].append(wordList[i])
        for word in self.graph.keys():
            self.graph[word] = list(sorted(self.graph[word], key = lambda k : self.diff(k, endWord)))

        self.visited[beginWord] = True
        self.bfs(beginWord)
        return self.min_path

    def diff(self, word1, word2):
        wlen = len(word1)
        diff = 0
        for i in range(wlen):
            if word1[i] != word2[i]:
                diff += 1
        return diff

    def bfs(self, v: str):
        queue = [[v]]
        visited = { v: 0}
        while len(queue) != 0:
            path, queue = queue[0], queue[1:]
            path_len = len(path)
            v = path[-1]
            if path_len > self.min_path_len:
                continue
            if path_len == self.min_path_len:
                if v == self.endWord and path not in self.min_path:
                    self.min_path.append(path)
                continue
            if v == self.endWord and len(path) < self.min_path_len:
                self.min_path = [path]
                self.min_path_len = path_len
                continue
            for w in self.graph[v]:
                if w in visited and visited[w] < path_len + 1:
                    continue
                queue.append(path + [w])
                visited[w] = path_len + 1
        return

if __name__ == '__main__':
    s = Solution()
    #print(s.findLadders(beginWord="hit", endWord="cog", wordList =["hot","dot","dog","lot","log","cog"]))
