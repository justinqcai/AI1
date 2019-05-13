from __future__ import division
import random
import numpy as np

w = np.array([[2.0, 3.0],[-2.0,-4.0],[1.0,-1.0], [1.0,2.0],[-2.0,-1.0]])
setup = [3, 2, 2]
lam = .01
i = [10,20,30]
target = [2,1]
#w1 = np.array([[1,2],[-2,-1]])
def func(x):
		return x/10
class backprop:
	def __init__(self, i, out, setup, lam, func, w):
		#self.inp = i
		self.targ = out
		self.setup = setup
		self.aval = np.array([None] * sum(setup))
		for x in range(len(i)):
			self.aval[x] = i[x]
		self.dval = np.array([None]*sum(setup[1:]))
		self.lam = lam
		self.func = func
		self.w = w

	def get_col(self, x, w):
		ar = []
		if x < self.setup[0]-1:
			for y in range(self.setup[0]):
				ar.append(w[y][x])
		else:
			for y in range(self.setup[0],sum(self.setup[0:2])):
				ar.append(w[y][x-self.setup[0]+1])
		return np.array(ar)
	def next_col(self, w):
		count = 0
		for x in w:
			if x != None:
				count+=1
		if count != sum(self.setup):
			c = 0
			for x in range(len(self.setup)):
				c+=setup[x]
				if c > count:
					return x
		else:
			return -1
	def dot(self, col, val):
		temp = []
		for x in range(sum(self.setup[:col]), sum(self.setup[:col+1])):
			temp.append(self.aval[x])
		ar = np.array(temp)
		fnl = 0
		for x in range(len(ar)):
			fnl+=(ar[x]*self.get_col(val,w)[x])
		return fnl
	def prop(self, col):
		if col > len(self.setup)-1:
			self.delta()
		else:
			#col = self.setup[self.next_col(self.dval) + 1]
			for x in range(sum(self.setup[1:col+1]), sum(self.setup[1:col+2])):
				self.dval[x] = self.dot(col, x)
			self.bp(col)
	def bp(self, col):
		for x in range(sum(self.setup[1:col+1]), sum(self.setup[1:col+2])):
			self.aval[x+self.setup[0]] = func(self.dval[x])
		self.prop(col+1)
	def delta(self):
		self.d = [None] * sum(self.setup[1:])
		for x in range(sum(self.setup[:len(self.setup)-1]), sum(self.setup)):
			self.d[x-self.setup[0]] = self.func((target[x-sum(self.setup[:len(self.setup)-1])] - self.aval[x]))
		x = len(self.d) - 2
		while None in self.d:
			self.d[x-2] = self.func(self.d[x]*self.w[x+1][0]+self.d[x+1]*self.w[x+1][1])
			self.d[x-1] = self.func(self.d[x]*self.w[x+2][0]+self.d[x+1]*self.w[x+2][1])
		self.weight()
	def weight(self):
		self.neww = self.w
		for x in range(len(self.neww)):
			for y in range(len(self.neww[0])):
				if x <self.setup[0]:
					self.neww[x][y] += self.lam*self.aval[x]*self.d[y]
				else:
					self.neww[x][y] += self.lam*self.aval[x]*self.d[y+2]
	def error(self, error):
		total = 0
		for x in range(len(self.targ)):
			total += abs(self.aval[len(self.aval)-x-1]-self.targ[len(self.targ)-x-1])
		return total
def converge(bp, error):
	b = bp
	while b.error(error) > error:
		b = backprop(i, target, setup, lam, func, b.neww)
		b.prop(0)
	return b
bp = backprop(i, target, setup, lam, func, w)
bp.prop(0)
bp = converge(bp, .0001)

print(bp.aval)
# print(bp.dval)
# print(bp.d)
print(bp.neww)


