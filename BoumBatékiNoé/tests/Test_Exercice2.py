import unittest
from src.Exercice2 import FIFO

class TestFIFO(unittest.TestCase):
	def setUp(self):
		self.fifo = FIFO()
		
	def test_AppendPop(self):
		self.fifo.append(11)
		self.assertEqual(self.fifo.pop(), 11)
		self.fifo.append(144)
		self.fifo.append(95)
		self.assertEqual(self.fifo.pop(), 144)
		self.assertEqual(self.fifo.pop(), 95)
		 
	def test_len(self):
		self.assertEqual(self.fifo.__len__, 0)
		self.fifo.append(4)
		self.assertEqual(self.fifo.__len__, 1)
		self.fifo.append(48)
		self.fifo.append(44)
		self.fifo.append(78)
		self.fifo.append(47)
		self.assertEqual(self.fifo.__len__, 5)

if __name__ == '__main__':
    unittest.main()
