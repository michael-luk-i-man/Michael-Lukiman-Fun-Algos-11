# FA11 3 

# Let's get Krusky. 

# MakeSet, FindSet, Union (heap?) 

# Hint: connecting root of shallower tree to deeper tree.

def MST_Kruskal(G,w):
	A = []
	for vertex in G.v:
		make_set(vertex)

	w = quicksort(nondecreasing order, w)

	# m log n for m edges

	for e in G.e:
		if find_set(e.u) != find_set(e.v): # at most 2m finds, each log n
			A = union(A, e) # upper bound of n - 1 vertices

	return A

# dominated by O(2m log n)

def make_set(G):
	all = []
	for vertex in G.v:
		new_tree(vertex) 

def find_set(tree, node):
	# u = tree[node]
	# depth_counter = 0
	# while u.pi != NIL:
	# 	depth_counter += 1
	# 	u.pi = u 
	return binary_tree_search(tree, node)

	# O(ln(n)) 
	# Depth of a node is the amount of times set was redirected. 
	# Since it's always merged with a larger, sets at least double with each redirection.



def union(s1,s2):
	if len(s1) <= len(s2):	
		small = s1
	combined[i] = 
