# FA11 2 

# Weights are integer values between 1 and W, inclusive. 

def MST_known_integers():
	sorted_w = counting_sort(w)

	for u in G.v:
		u.key = inf 
		u.pi = NIL

	Q = G.v

	while Q != []:
		if sorted_w[0].v in Q:
			sorted_w[0].u = u
			sorted_w[0].v.pi = sorted_w[0].u

			Q.remove(u)
			sorted_w.remove(sorted_w[0])

			

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
