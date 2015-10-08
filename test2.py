import unittest
from problem2 import solution

class TestProblem1(unittest.TestCase):


	def test1(self):
		# Example case
		N = 3245
		self.assertEqual(solution(N), 55)

	def test2(self):
		# Example case
		N = 50
		self.assertEqual(solution(N), 10)

	def test3(self):
		# Example case
		N = 286
		self.assertEqual(solution(N), 22)

	def test4(self):
		# Binary root equals sqrt(N)
		N = 25
		self.assertEqual(solution(N), 5)

	def test5(self):
		# No solution
		N = 19
		self.assertEqual(solution(N), -1)

	def test6(self):
		# No solution
		N = 113
		self.assertEqual(solution(N), -1)

	def test7(self):
		# Symmetric square
		N = 17*17
		self.assertEqual(solution(N), 17)


if __name__ == '__main__':
	unittest.main()