import math
class Exercice1:
	@staticmethod
	def TroisGrandNombre(numbers: list[int]) -> list[int]:
		return sorted(numbers, reverse=True)[:3]
	
	@staticmethod
	def PremierOuNon(number: int) -> bool:
		if number == 1: #Exception 
			return True
		if number == 2: #Exception 
			return False
		if number == 4: #Exception 
			return False
		for i in range(2, math.ceil(number*0.5)):
			if number % i == 0:
				return False
		return True
	
	@staticmethod
	def ArithmeOuPas(numbers: list[int]) -> bool:
		pass
