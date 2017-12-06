# FA11 2 

# Weights are integer values between 1 and W, inclusive. 

def MST_known_integers():
	sorted_w = counting_sort(w,max_w)

	Qw = sorted_w
	Qe = []
	Qv = G.v

	for u in G.v:
		u.key = inf
		u.pi = NIL
		for v in G.adj[u]:
			Qe.append({u,v}) # could have repeat edges in other directionm so O(V(V-1)/2)

	while Qv != []:
		weight_to_find = dequeue(Qw) # Already sorted so can just dequeue.
		find_edge(G,Qe,weight_to_find) 

def find_edge(G,Qe,weight_to_find):
	for edge in Qe:
		if w(edge) = weight_to_find and edge[1] in Qv: # Find the lightest edge connecting to a separated vertex.
			edge[1].pi = edge[0] # v.pi of edge is u
			edge[1].key = w(edge)
			Qv.remove(v) # v is accounted for in the tree with the smallest weight connected to it 
			return 

			

# Counting Sort Base Algorithm
def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array # and count, if needed.


# Prim's Base Algorithm

def MST_prim(G, w, r):
	for u in G.v:
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
