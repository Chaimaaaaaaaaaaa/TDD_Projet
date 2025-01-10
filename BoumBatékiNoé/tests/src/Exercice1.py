import math
class Exercice1:
	@staticmethod
	def TroisGrandNombre(numbers: list[int]) -> list[int]:
		return sorted(numbers, reverse=True)[:3]
	
	@staticmethod
	def PremierOuNon(number: int) -> bool:
		if number == 1: #Execption 
			return True
		for i in range(2, math.ceil(number**0.5)):
			if number % i == 0:
				return False
		return True
	
	@staticmethod
	def ArithmeOuPas(numbers: list[int]) -> bool:
		pass
