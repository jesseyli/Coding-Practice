import unittest
from problem1.py import solution

class TestProblem1(unittest.TestCase):

	def setUp(self):
		pass

	def test1(self):
		# Example case
		A = [1.0, 0.1, -1.0, -7.0, 3.0, -5.0, -2.5, 0.0, 1.0]
		self.assertEqual(solution(A), 262.5)

	def test2(self):
		# Product goes over 10^9
		A = [-0.00001, 1000.0, 1000.0, 1000.0, 1000.0, -100.0, 0.000001]
		self.assertEqual(solution(A), 1e9)


if __name__ == '___main__':
	unittest.main()