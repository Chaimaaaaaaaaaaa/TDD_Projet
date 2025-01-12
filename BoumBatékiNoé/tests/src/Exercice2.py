import queue

class FIFO:
	def __init__(self):
		self.queue = queue.Queue()
	def taille(self):
		return self.queue.qsize()
	def plus(self, x:int):
		self.queue.put(x)
	def minus(self):
		return self.queue.get()
