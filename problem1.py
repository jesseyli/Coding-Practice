# This problem can be solved by finding the maximum of the maximum products that end at each
# index of A.  Let maxProd(A[i]) be the maximum product that ends at A[i] and let minProd(A[i])
# be the minimum product that ends at A[i].  At each index i, the maximum product will either be
# A[i], A[i]*minProd(A[i-1]), or A[i]*maxProd(A[i-1]).  We can start at the beginning of the array
# and iterate through while keeping track of the previous maxProd, minProd, and best found so far
# to find the maximum product of any slice with a single pass through the array.  

def solution(A):
	# Return the maximum product of any slice in A. 
	maxCurr, minCurr, output = A[0],A[0],A[0]
	for a in A[1:]:
		if output >= 1e9:
			return 1e9
		prevMax = maxCurr
		maxCurr = max(maxCurr*a,a,minCurr*a)
		minCurr = min(prevMax*a,a,minCurr*a)
		output = max(output,maxCurr)
	return output

