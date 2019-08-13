# python3
import sys, threading
from collections import deque, defaultdict
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
    def compute_height(self):
        nodes = defaultdict(set)
        for i in range(self.n):
            if self.parent[i] == -1: root = i
            else: nodes[self.parent[i]].add(i)
        if nodes == None:return
        q, level, target, active= deque([root]), 0, root, 0
        while q:
            node = q.popleft()
            if node == target:
                level, active = level + 1, 1
            if nodes[node] != []:
                for i, child in enumerate(nodes[node]):
                    q.append(child)
                if active == 1 and q:
                    target, active = q[-1], 0
        return level
def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())
threading.Thread(target = main).start()
