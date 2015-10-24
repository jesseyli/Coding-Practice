import pdb

def solution(A,X,D):
	furthest = D
	leaves = []
	for i in range(0,X):
		leaves.append(False)
	for k in range(0,len(A)):
		leaves[A[k]] = True
		if furthest >= X:
			return k
		if A[k] > furthest - D and A[k] <= furthest:
			far_leaf = A[k]
			furthest = A[k] + D
			i = 1
			while i < D + 1:
				if i + far_leaf < X and leaves[i + far_leaf]:
					far_leaf += i
					furthest = far_leaf + D
					i = 0
				if furthest >= X:
					return k
				i += 1
	if furthest >= X:
		return 0
	return -1
