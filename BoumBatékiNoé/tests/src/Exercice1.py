import math
class Exercice1:
	@staticmethod
	def TroisGrandNombre(x: list[int]) -> list[int]:
		return sorted(x, reverse=True)[:3]
	
	@staticmethod
	def PremierOuNon(x: int) -> bool:
		if x == 1: #Exception 
			return True
		if x == 2: #Exception 
			return False
		if x == 4: #Exception 
			return False
		for i in range(2, math.ceil(x*0.5)):
			if x % i == 0:
				return False
		return True
	
	@staticmethod
	def ArithmeOuPas(x: list[int]) -> bool:
		diff = x[1] - x[0]
		for i in range(1, len(x)):
			if x[i] - x[i - 1] != diff:
				return False
		return True
