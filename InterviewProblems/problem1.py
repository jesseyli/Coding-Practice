def solution(A):
	# Return the maximum product of any slice in A. Iterates through A finding the smallest negative
	# product and largest positive product at each array index.
	max_pos, min_neg, output = 1.0
	if not A:
		return 0
	for a in A:
		if output > 1e9:
			return 1e9
		if a > 0:

		elif a < 0:
		elif a == 0:
			

		