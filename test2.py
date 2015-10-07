import unittest
from problem2 import solution

class TestProblem1(unittest.TestCase):


	def test1(self):
		# Example case
		N = 3245
		self.assertEqual(solution(A), 55)


if __name__ == '__main__':
	unittest.main()