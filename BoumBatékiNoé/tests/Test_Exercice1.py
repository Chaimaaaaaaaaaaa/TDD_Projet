import unittest
from src.Exercice1 import Exercice1

class TestExercice1(unittest.TestCase):
	
	def setUp(self):
		self.exercice1 = Exercice1()
	
	#Tests Nombres Plus Grands
	def test_NPG(self):
		self.assertEqual(self.exercice1.TroisGrandNombre([1,2,3,4,5,6]), [4,5,6])
		self.assertEqual(self.exercice1.TroisGrandNombre([0,1,1,2,3,4,5,6,6]), [5,6,6])
		self.assertEqual(self.exercice1.TroisGrandNombre([-99,1,0,-1]), [-1,0,1])
	
	#Tests Premier ou non
	def test_PON(self):
		self.assertTrue(self.exercice1.PremierOuNon(1))
		self.assertTrue(self.exercice1.PremierOuNon(3))
		self.assertTrue(self.exercice1.PremierOuNon(5))
		self.assertTrue(self.exercice1.PremierOuNon(7))
		self.assertTrue(self.exercice1.PremierOuNon(11))
		self.assertFalse(self.exercice1.PremierOuNon(2))
		self.assertFalse(self.exercice1.PremierOuNon(4))
		self.assertFalse(self.exercice1.PremierOuNon(6))
		self.assertFalse(self.exercice1.PremierOuNon(4754516))
	
	#Tests Arithmétique 
	def test_AOP(self):
		self.assertTrue(self.exercice1.ArithmeOuPas([1,2,3,4,5,6]))
		self.assertTrue(self.exercice1.ArithmeOuPas([1,6,11,16]))
		self.assertFalse(self.exercice1.ArithmeOuPas([1,3,3,4,5,6]))
		self.assertTrue(self.exercice1.ArithmeOuPas([2,4,8,16,32]))

if __name__ == '__main__':
    unittest.main()
