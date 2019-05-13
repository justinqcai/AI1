from __future__ import division
import percy as p
import Perceptron as f
import random
import math


x = p.Input()
y = p.Input()
left = p.percy([1, 0], -1.5)
right = p.percy([-1, 0], -1.5)
bottom = p.percy([0, 1], -1.5)
top = p.percy([0, -1], -1.5)
side = p.percy([1, 1], 1.5)
tb = p.percy([1, 1], 1.5)
circ = p.percy([1, 1], 1.5)
left.set_input([x, y])
right.set_input([x, y])
top.set_input([x,y])
bottom.set_input([x,y])
side.set_input([right, left])
tb.set_input([top, bottom])
circ.set_input([side, tb])
count = 0
for h in range(10000):
	x.set_input((random.random()*3)-1.5)
	y.set_input((random.random()*3)-1.5)
	xor = circ
	c = xor.eval()
	if c> .53:
		c = 1
	else:
		c = 0
	rv = math.sqrt((x.eval()**2)+(y.eval()**2))
	if rv<=1:
		rv=1
	elif rv>1:
		rv=0
	if rv==c:
		count+=1
	print(c)
print(count/100)
