from __future__ import division
import percy as p
import Perceptron as f
import random
import numpy as np
import math
import matplotlib as py

def rand():
	return random.random()*2-1
def rand2():
	x = random.random()
	if x > .5:
		return 1
	else:
		return -1
final = [0, 1, 1, 0]
ar = np.array([rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()])
def method(ar):
	x = p.Input()
	y = p.Input()
	n1 = p.percy([ar[0], ar[1]], ar[2])
	n2 = p.percy([ar[3], ar[4]], ar[5])
	n3 = p.percy([ar[6], ar[7]], ar[8])
	n1.set_input([x, y])
	n2.set_input([x, y])
	n3.set_input([n1, n2])
	xor = n3
	out = []
	for a in range(2):
		for b in range(2):
			x.set_input(a)
			y.set_input(b)
			out.append(xor.eval())
	return out
def test(out, final):
	fnl = 0
	for x in range(len(out)):
		fnl += abs(final[x]-out[x])
	return fnl
#error = test(method(ar), final)
done = False
lambdas = []
iterations = []
learn = .7
# while learn <= 1:
# 	done = False
while done is False:
	direc = np.array([rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()])
	error = test(method(ar), final)
	new_ar = ar+(direc*learn)
	if error>test(method(new_ar), final):
		for x in range(100):
			if done is False:
				new_ar += (direc*learn)
				error = test(method(new_ar), final)
				if error < .01:
					#print(x, new_ar, error, method(new_ar))
					#lambdas.append(learn)
					#iterations.append(x)
					#learn+= .1
					print(x)
					done = True
#py.plot(iterations, lambdas)