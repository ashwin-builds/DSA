from collections import defaultdict
from collections import deque

# Array of edges (directed: [start, end]):

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Array of edges -> Adjacency Matrix:

M = []
for i in range(n):
	M.append([0] * n)

for u, v in A:
	M[u][v] = 1
	# If the graph was undirected, uncomment the following:
	# M[v][u] = 1
	# With an undirected graph, you get a symmatric matrix along the diagonal.

# Array of edges -> Adjacency List (most common):
D = defaultdict(list)

for u,v in A:
	D[u].append(v)
	# If the graph was undirected, uncomment the following:
	# D[v].append(u)

# DFS with recursion - O(V + E) where V = no. of nodes; E = no. of edges

def dfs_recursive(node):
	print(node)
	for nei_node in D[node]:
		if nei_node not in seen:
			seen.add(nei_node)
			dfs_recursive(nei_node)

source = 0 # starting node
seen = set()
seen.add(source)
dfs_recursive(source)

# DFS with iteration - O(V + E) where V = no. of nodes; E = no. of edges

source = 0
seen = set()
seen.add(source)

stack = [source] # analogous to call stack

while stack:
	node = stack.pop()
	print(node)
	for nei_node in D[node]:
		if nei_node not in seen:
			seen.add(nei_node)
			stack.append(nei_node)

# NOTE: We still get a DFS, but it is a different output to 
#		the one with recursion because we first add each node
#		to the stack before processing any given one.

# BFS with queue - O(V + E) where V = no. of nodes; E = no. of edges
# Note: It is the same as BFS iteration but uses a queue and popleft
source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
	node = q.popleft()
	print(node)
	for nei_node in D[node]:
		if nei_node not in seen:
			seen.add(nei_node)
			q.append(nei_node)

# Represing a graph node using a class
class Node:
	def __init__(self, val):
		self.val = val
		self.neighbors = []

	def __str__(self):
		return f'Node({self.val})'

	def display(self):
		connections = [node.val for node in self.neighbors]
		return f'{self.val} is connected to: {connections}'

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(B.display())

