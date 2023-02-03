

def comb(L):
	
	for i in range(4):
		for j in range(4):
			for k in range(4):
				
				
				if (i!=j and j!=k and i!=k):
					print(L[i], L[j], L[k])
					

comb([1,4,5,6])
