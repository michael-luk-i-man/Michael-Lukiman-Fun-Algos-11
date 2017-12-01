# FA11 1.1

# Weights of undirected graph G all value w. Create algorithm to make MST. 


# 1.2 One weight that's not like the others. 

MST-odd-one-out(G,w): 
	normal_weight, special_weight = determine_normal_weight()

	if special_weight > -1:
	w.remove(0)
	w.remove(1)




determine_normal_weight(w): # returns normal weight (and special weight if found within the first two elements. else -1). 

	if len(w) < 3: # If less than three elements... 
		return w[0], -1 # Normalcy is arbitrary, can say first is normal.

	if w[0] == w[1]: # If the first two elements are the same, they share the normal weight (since there's only one element that will not have the normal weight).
		return w[0], -1  # Return the normal.

	if w[1] == w[2]: # If the function continues, that means index 0 and 1 have different weights, therefore one of them is the special weight. If index 1 and 2 are the same, then index 0 is the special weight, and that's good news for the running time. We have an additional thing to return, which is the special weight.
		return w[1], w[0]

	else: # If the function still continues, then w[1] is the special one, because given the nature of the list, w[2] will be be the same as w[0]. (While this relies on the integrity of the input, this function is only for the given problem to minimize running time.)
		return w[2], w[1]

	





Generic-MST:(G, w):
	A = []
	while len(A) != len(w):

	