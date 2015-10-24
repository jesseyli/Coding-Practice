import unittest
from frog import solution
import itertools

class TestProblem1(unittest.TestCase):


	def test1(self):
		# Example case 1
		a = [1,3,1,4,2,5]
		x = 7
		d = 3
		self.assertEqual(solution(a,x,d), 3)

	def test2(self):
		# Example case 2
		a = [6,5,4,3]
		x = 7
		d = 3
		self.assertEqual(solution(a,x,d), 3)

	def test3(self):
		# Example case 3
		a = [2, 5, 10, 8]
		x = 13
		d = 3
		self.assertEqual(solution(a,x,d), 3)

	def test4(self):
		# Example case 4
		a = [3, 5, 1, 4]
		x = 6
		d = 2
		self.assertEqual(solution(a,x,d), 2)

	def test5(self):
		# all perms of 3 leaves, d = 1
		all_perm = itertools.permutations([1,2,3])
		results = []
		x = 4
		d = 1
		for perm in all_perm:
			results.append(solution(perm,x,d))
		self.assertEqual(results, [2,2,2,2,2,2])

	def test6(self):
		# Frog can never jump across
		a = [1,3,1,4,2,5]
		x = 9
		d = 3
		self.assertEqual(solution(a,x,d), -1)

	def test7(self):
		# all perms of 3 leaves, d = 2
		all_perm = itertools.permutations([1,2,3])
		results = []
		x = 4
		d = 2
		for perm in all_perm:
			print perm
			results.append(solution(perm,x,d))
		self.assertEqual(results, [1,1,0,0,1,1])

	def test8(self):
		# Empty array
		a = []
		x = 1
		d = 3
		self.assertEqual(solution(a,x,d), 0)


if __name__ == '__main__':
	unittest.main()