import unittest
from problem1 import solution

class TestProblem1(unittest.TestCase):


	def test1(self):
		# Example case
		A = [1.0, 0.1, -1.0, -7.0, 3.0, -5.0, -2.5, 0.0, 1.0]
		self.assertEqual(solution(A), 262.5)

	def test2(self):
		# Product goes over 10^9
		A = [-0.00001, 1000.0, 1000.0, 1000.0, 1000.0, -100.0, 0.000001]
		self.assertEqual(solution(A), 1e9)

	def test3(self):
		# Array of zeros
		A = [0.0,0.0,0.0,0.0]
		self.assertEqual(solution(A), 0)

	def test4(self):
		# All negative values
		A = [-1.0, -2.0, -3.0, -0.5, -0.25, -10.0]
		self.assertEqual(solution(A),7.5)

	def test5(self):
		# Single negative value and zeros
		A = [-5,-5, 0, 0, 0, 0]
		self.assertEqual(solution(A),25)

	def test6(self):
		# All negative values less than 1
		A = [-0.1, -0.2, -0.3, -0.5, -0.25, -0.25]
		self.assertEqual(solution(A),0.15)

	def test7(self):
		# Single item array
		A = [15.0]
		self.assertEqual(solution(A),15)

if __name__ == '__main__':
	unittest.main()