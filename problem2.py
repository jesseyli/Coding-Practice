from math import sqrt,ceil
# Bit_rev will always be an odd number since zeros at end of N will be lost upon flipping. Let A be
# some symmetric binary root to integer N, so that N = A*bit_rev(A). Let x be the smallest number of
# right shifts that makes N an odd number. bit_rev(A>>x) = bit_rev(A) since zeros are removed upon
# flipping. We can then get (N>>x) = (A>>x)*bit_rev(A>>x) since bit_rev is always odd. From here we
# see that (A>>x) must be odd as well, which would mean that (A>>x) = bit_rev(bit_rev(A>>x)).  We
# therefore know that the smaller of (A>>x) and bit_rev(A>>x) must be less than or equal to the
# square root of (N>>x).  Since we only need to check numbers from 1 to (N>>x) to find the symmetric
# binary root of N, the time complexity is bounded by O(sqrt(N)).  

def solution(N):
	# Finds smallest symmetric binary root and returns it, returns -1 if there is none
	def bit_rev(A):
		# Takes in an integer N and returns its value after reversing binary bits
		return int('0b' + bin(A)[:1:-1], 2)
	zeros = 0
	while N % 2 == 0:
		N = N/2
		zeros += 1
	for i in range(1,int(ceil(sqrt(N*pow(2,zeros))))+1):
		if i*bit_rev(i) == N:
			return i*pow(2,zeros)
	return -1

