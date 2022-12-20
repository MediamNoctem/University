#-*- coding: utf-8 -*-
import random
import math

import pybee

class spherebee (pybee.floatbee):
	"""Функция - сумма квадратов по каждой координате"""
			
	# Количество координат
	count = 2
	
	@staticmethod
	def getstartrange ():
		return [150.0]  * spherebee.count
	
	@staticmethod
	def getrangekoeff ():
		return [0.98]  * spherebee.count		
		
	def __init__ (self):
		pybee.floatbee.__init__ (self)
	
		self.minval = [-150.0] * spherebee.count
		self.maxval = [150.0] * spherebee.count

		self.position = [random.uniform (self.minval[n], self.maxval[n]) for n in range (spherebee.count) ]
		self.calcfitness()
		
	def calcfitness (self):
		"""Расчет целевой функции. Этот метод необходимо перегрузить в производном классе. 
		Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
		Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
		self.fitness = 0.0
		for val in self.position:
			self.fitness -= val * val

###################################################	

class Himmelblaybee(pybee.floatbee):
	count = 2

	@staticmethod
	def getstartrange():
		return [6.0] * Himmelblaybee.count

	@staticmethod
	def getrangekoeff():
		return [0.9] * Himmelblaybee.count

	def __init__(self):
		pybee.floatbee.__init__(self)
		self.minval = [-6.0] * Himmelblaybee.count
		self.maxval = [6.0] * Himmelblaybee.count
		self.position = [random.uniform(self.minval[n], self.maxval[n]) for n in range(Himmelblaybee.count)]
		self.calcfitness()

	def calcfitness(self):
		"""Расчет целевой функции. Этот метод необходимо перегрузить в производном классе.
        Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
        Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
		self.fitness = -Himmelblaybee.fun(self.position[0], self.position[1])

	@staticmethod
	def fun(x1, x2):
		return (x1 * x1 + x2 - 11) ** 2 + (x1 + x2 * x2 - 7) ** 2


class Rastriginbee(pybee.floatbee):
	count = 2

	@staticmethod
	def getstartrange():
		return [5.0] * Rastriginbee.count

	@staticmethod
	def getrangekoeff():
		return [0.9] * Rastriginbee.count

	def __init__(self):
		pybee.floatbee.__init__(self)
		self.minval = [-5.0] * Rastriginbee.count
		self.maxval = [5.0] * Rastriginbee.count
		self.position = [random.uniform(self.minval[n], self.maxval[n]) for n in range(Rastriginbee.count)]
		self.calcfitness()

	def calcfitness(self):
		"""Расчет целевой функции. Этот метод необходимо перегрузить в производном классе.
        Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
        Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
		self.fitness = -Rastriginbee.fun(self.position[0], self.position[1])

	@staticmethod
	def fun(x1, x2):
		return 20 + x1 ** 2 - 10 * math.cos(2 * math.pi * x1) + x2 ** 2 - 10 * math.cos(2 * math.pi * x2)

###################################################

class rosenbrockbee (pybee.floatbee):
	"""Функция Rosenbrock"""
		
	# Количество координат
	count = 2
	
	@staticmethod
	def getstartrange ():
		return [10.0]  * rosenbrockbee.count
		
	@staticmethod
	def getrangekoeff ():
		return [0.98]  * rosenbrockbee.count	
		
	def __init__ (self):
		pybee.floatbee.__init__ (self)
		
		self.minval = [-10.0] * rosenbrockbee.count
		self.maxval = [10.0] * rosenbrockbee.count

		
		self.position = [random.uniform (self.minval[n], self.maxval[n]) for n in range (rosenbrockbee.count) ]
		self.calcfitness()
		
	def calcfitness (self):
		"""Расчет целевой функции. Этот метод необходимо перегрузить в производном классе. 
		Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
		Эту функцию необходимо вызывать после каждого изменения координат пчелы"""

		self.fitness = 0.0
		for n in range (1):
			xi = self.position[n]
			xi1 = self.position[n + 1]
			
			self.fitness -= 100.0 * ( ( (xi * xi - xi1) ** 2)  + ( (1 - xi) ** 2 ))
