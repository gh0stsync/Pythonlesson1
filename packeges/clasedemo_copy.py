#!/usr/bin/env python

class Calculator :
	
	def __init__(self, ina, inb) :
		self.a = ina
		self.b = inb

	def add(self) :
		return self.a + self.b

	def mul(self) :
		return self.a * self.b





class SciCal(Calculator) :

	def power(self) :
		return pow(self.a, self.b) 




def QuickAdd(a, b) :
	return a + b 



