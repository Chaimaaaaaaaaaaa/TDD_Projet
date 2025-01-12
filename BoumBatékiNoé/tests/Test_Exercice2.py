import unittest
from src.Exercice2 import FIFO

class TestFIFO(unittest.TestCase):
	def setUp(self):
		self.queue = FIFO()
		
	def test_AppendPop(self):
		self.queue.plus(11)
		self.assertEqual(self.queue.minus(), 11)
		self.queue.plus(144)
		self.queue.plus(95)
		self.assertEqual(self.queue.minus(), 144)
		self.assertEqual(self.queue.minus(), 95)
		 
	def test_len(self):
		self.assertEqual(self.queue.taille(), 0)
		self.queue.plus(4)
		self.assertEqual(self.queue.taille(), 1)
		self.queue.plus(48)
		self.queue.plus(44)
		self.queue.plus(78)
		self.queue.plus(47)
		self.assertEqual(self.queue.taille(), 5)

if __name__ == '__main__':
    unittest.main()
