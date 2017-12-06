# FA11 1.1

# Weights of undirected graph G all value w. Create algorithm to make MST. 


# 1.1 Homogenous nodes. 

def MST_homogeneous(G,w):

	Q = G.v
	u = dequeue(Q)
	u.key = 0

	while Q != []:
		v = dequeue(Q)
		v.pi = u
		v.key = w 
		u = v 

# Way faster than Prim, at V steps. 

# 1.2 One weight that's not like the others. 

def MST_odd_one_out(G,w): 

	# if len(G.v) < len(G.e):
	# 	adjacency_search = 'fib_heap'
	# else:
	# 	adjacency_search = 'binary_heap'

	normal_weight, special_weight = determine_normal_weight(w)
	special_weight = determine_special_weight(w, special_weight)
	w = normal_weight

	if normal_weight => special_weight:
		Q = G.v
		u = dequeue(Q)
		u.key = 0

		while len(Q) > 1: # While there's more than one element queued
			if Q[0] in G.adj[u] and w(u,Q[0]) == normal_weight: # Assume Q dequeues from front. If we prioritize the normal weight: 
				v = dequeue(Q) 
				v.pi = u
				v.key = w 
				u = v 
			else: # If it's not the normal weight, then the vertex gets moved to the back of the queue. 
				Q.append(dequeue(Q))

		v = dequeue(Q) # The last element is either unreachable by normal weights via the tree we've made so far or it is simply the last element without any rearrangement, thus we see if there are any normal adjacent weights:
			
		global key 	
		if any_adj_normals(G,v) != True: # ...if not true that means there is only one edge from the vertex and it is the special weight. 
			v.pi = key
			v.key = special_weight

	else: # We prefer the special weight if we can see it. 
		for u in G.v:
			for v in G.adj[u]: # Max V(V-1)/2 if graph is strongly connected. 
				if w(u,v) = special_weight: # Find that weight.
					v.pi = u 
					v.key = special_weight
					key_G = G
					G.v.remove(u)
					G_prime = G
					G = key_G
					MST_homogeneous(G_prime) # Run the uniform w algorithm after making the first connection with w'. 

def any_adj_normals(G,v):
	for x in G.adj[v]:
		if w(x,v) == normal_weight: # If there is a normal weight we make the other vertex the parent of v. 
			v.pi = x
			v.key = w
			return True
		if w(x,v) == special_weight:
			global key
			key = x
			return False

				
def determine_special_weight(w, special_weight):

		if special_weight == 'none_yet':
			for weight in w:
				if weight != normal_weight:
					special_weight = weight
					return special_weight
		else:
			return special_weight


def determine_normal_weight(w): # returns normal weight (and special weight if found within the first two elements. else 'none_yet'). 

	if len(w) < 3: # If less than three elements... 
		return w[0], w[0] # Normalcy is arbitrary, can say first is normal and special.

	if w[0] == w[1]: # If the first two elements are the same, they share the normal weight (since there's only one element that will not have the normal weight).
		return w[0], 'none_yet'  # Return the normal.

	if w[1] == w[2]: # If the function continues, that means index 0 and 1 have different weights, therefore one of them is the special weight. If index 1 and 2 are the same, then index 0 is the special weight, and that's good news for the running time. We have an additional thing to return, which is the special weight.
		return w[1], w[0]

	else: # If the function still continues, then w[1] is the special one, because given the nature of the list, w[2] will be be the same as w[0]. (While this relies on the integrity of the input, this function is only for the given problem to minimize running time.)
		return w[2], w[1]

# Runtime takes V with the addition of the functions to determine the normal and special weight, taking maximum E additional steps, plus the last element in the queue, which can take an additional V-1 steps if it connects to all other nodes, and worst case if the special weight edge is the last in its adjacency list. Here we can use the heap searche for efficiency in the single search, though the algorithm would still be dominated by V + E. 