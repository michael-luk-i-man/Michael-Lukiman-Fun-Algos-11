# FA11 1.1

# Weights of undirected graph G all value w. Create algorithm to make MST. 


# 1.1 Homogenous nodes. 

def MST_homogenous(G,w):

	for u in G.v: 
		v = G.adj[u][0] # V is any arbitrary node connected to that node. 
		for adj in G.adj[u]:
			G.adj[adj].remove(u) # Remove all other edges coming out of u so there are no backedge repeats. 
		v.pi = u # Parent of v is u.  
		v.key = w(u,v) # Key of v is the weight of connecting edge. 
		u = v # New pass, where v is the new u. Loop continues to grow tree.

		# Insert all edges are safe meme.

		# Way faster than Prim, where V is the number of nodes and E is the number of edges, requiring O((V-1) + E) steps.  


# 1.2 One weight that's not like the others. 

def MST_odd_one_out(G,w): 

	normal_weight, special_weight = determine_normal_weight(w)
	special_weight = determine_special_weight(w, special_weight)
	
	u = special_weight.u
	special_weight.v.pi = u

	# The first link is made between two nodes. The tree right now is two nodes and the edge between them. 

	for adj in G.adj[u]:
		G.adj[adj].remove(u) # Ignore chances for redundant edge checks. 


	G_prime = G 
	G_prime.remove(u) # Ignore the parent. 
	w_prime = w
	w_prim.remove(w) # Ignore the already included edge		

	MST_homogenous(G_prime, w_prime) # Run homogenous MST. 

	# Running time of homogenous except with a potential (E + 4) additional comparisons due to determine_normal and determine_special_weight.


				
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

# Prim's Base Algorithm

def MST_prim(G, w, r):
	for each u in G.v:
		u.key = inf
		u.pi = NIL

	r.key = 0

	Q = G.v # minimum priority queue

	while Q != []:
		u = extract_min(Q):
		for each v in G.adj[u]:
			if v in Q and w(u,v) < v.key
				v.pi = u
				v.key = w(u,v)

# with binary search

def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

	