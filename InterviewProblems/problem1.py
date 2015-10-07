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

