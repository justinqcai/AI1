from __future__ import division
import numpy as np
import math
from random import random
from random import shuffle

#training = [[np.array([0, 0, 1]), 0], [np.array([0, 1, 1]), 0], [np.array([1, 0, 1]), 0], [np.array([1,1, 1]), 1]]
def cre_set(size):
	training = []
	l = int(math.pow(2, size))
	for x in range(int(math.pow(2, l))):
		ar = str(dec_to_bin(x, l))
		training.append(create_set(size, ar))
	return training
def spe_cre(size, lim):
	training = []
	l = int(math.pow(2, size))
	nums = []
	for x in range(l):
		nums.append(x)
	for x in range(lim):
		temp = nums
		shuffle(temp)
		num = temp[0]
		nums.remove(num)
		#ar = str(dec_to_bin(x, l))
		training.append(special_set(num, size))
	return training
def special_set(num, size):
	training = []
	ar = str(dec_to_bin(num, size))
	temp1 = []
	for y in ar:
		temp1.append(int(y))
	freq = {temp1.count(a): a for a in set(temp1)}
	out = freq[max(freq)]
	temp1.append(1)
	training.append(np.array(temp1))
	training.append(out)
	return training

def dec_to_bin(num, length):	
	return ("{:0" + str(length) + "b}").format(num)
def create_set(size, out):
	training = []
	for x in range(int(math.pow(2, size))):
		ar = str(dec_to_bin(x, size))
		temp = []
		temp1 = []
		for y in ar:
			temp1.append(int(y))
		temp1.append(1)
		temp.append(np.array(temp1))
		temp.append(int(out[x]))
		training.append(temp)
	return training
def spe_perceptron(training):
	w = np.array([random() for x in range(len(training[0][0]))])
	learn_rate = 1
	for y in range(50):
		for epoch in training:
			f = learn_rate * step(epoch[0].dot(w))
			w += (epoch[1] - f)*epoch[0]
	return w
def perceptron_learn(training):
	w = [np.array([random() for x in range(len(training[0][0][0]))]) for y in range(len(training))]
	learn_rate = 1
	for x in range(len(training)):
		for y in range(50):
			for epoch in training[x]:
				f = learn_rate * sigmoid(epoch[0].dot(w[x]))
				w[x] += (epoch[1] - f)*epoch[0]
	return w
def step(a):
	if a > 0:
		return 1
	else:
		return 0
def sigmoid(a):
	#b = (1/(1+math.exp(-3*a)))
	return 1/(1+math.exp(-3*a))
def test(ts, w):
	numi = 0
	for i in ts:
		n = sigmoid(i[0].dot(w))
		if n >= .5:
			n = 1
		else:
			n = 0
		if n != i[1]:
			numi += 1
	return numi
# num = []
# acc = []
# size = 10
# lim = 10
# while lim <= 100:
# 	ts = spe_cre(size, lim)
# 	#print(ts)
# 	ls = spe_cre(size, lim)
# 	result = spe_perceptron(ts)
# 	numi = test(ls, result)
# 	corr = len(ts) - numi
# 	#print(corr, len(ts))
# 	num.append(lim)
# 	acc.append(corr/len(ts))
# 	lim += 10
# import matplotlib.pyplot as plt
# plt.plot(num, acc)
# plt.show()
def cre():
	fnl = []
	training = cre_set(2)
	result = perceptron_learn(training)
	corr = 0
	for x in range(len(result)):
		numi = test(training[x], result[x])
		if numi is 0:
			corr+= 1
			fnl.append(result[x])
	return fnl
	# 		print(training[x])
	# 		print(result[x])
	# print(corr)
