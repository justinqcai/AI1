import math
import numpy as np
class percy:
	def __init__(self,w,t):
		self.weight = w
		self.thresh = t
	def set_input(self, i):
		self.input = i
	def __int__(self):
		count = 0
		for x in range(len(self.weight)):
			count += int(self.input[x]) * self.weight[x]
		if count > self.thresh:
			return 1
		return 0
	def eval(self):
		count = 0
		for x in range(len(self.weight)):
			count += (self.input[x].eval()) * self.weight[x]
		return self.sigmoid(count-self.thresh)
		# store = []
		# for ink in self.input:
		# 	store.append(ink.eval())
		# tbr = self.sigmoid(np.dot(self.weight, store))
		# return tbr
	def sigmoid(self, a):
		#b = (1/(1+math.exp(-3*a)))
		return 1/(1+math.exp(-3*a))
class Input(percy):
	def __init__(self):
		self.value = 0
	def set_input(self, i):
		self.value = i
	def eval(self):
		return self.value
# n1 = percy([-1, 1], .5)
# n2 = percy([1, -1], .5)
# n3 = percy([1, 1], 0)
# n3.set_input([n1, n2])
# xor = n3
# for a in range(2):
# 	for b in range(2):
# 		n1.set_input([a,b])
# 		n2.set_input([a,b])
# 		print(a, b, int(xor))
# print("\n")
# n1 = percy([1, 1], 1.5)
# n2 = percy([-1, -1], -.5)
# n3 = percy([1, 1], 0)
# n3.set_input([n1, n2])
# xnor = n3
# for a in range(2):
# 	for b in range(2):
# 		n1.set_input([a,b])
# 		n2.set_input([a,b])
# 		print(a, b, int(xnor))

	# def set_value(v):
	# 	self.value = v
# x1 = Input()
# x2 = Input()
# node_3 = percy([w13,w23],t3)
# node_4 = percy([w14,w24],t4)
# node_5 = percy([w35,w45],t5)
# node_3.set_inputs([x1,x2])
# node_4.set_inputs([x1,x2])
# node_5.set_inputs([node_3, node_4])
# xor = node_5
# for a in range(2):
# 	for b in range(2):
# 		x1.set_value(a)
# 		x2.set_value(b)
# 		print(a, b, xor.eval())