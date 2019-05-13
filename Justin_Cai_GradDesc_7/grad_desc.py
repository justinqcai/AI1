import random
import math
import matplotlib.pyplot as plt
def find_min(func, bottom, top, error):
	lim = top-(top-bottom)*((math.sqrt(5)-1)/2)
	lim1 = bottom +(top-bottom)*((math.sqrt(5)-1)/2)
	if (top-bottom) <= error:
		return bottom
	if func(lim)<func(lim1):
		return find_min(func, bottom, lim1, error)
	else:
		return find_min(func, lim, top, error)
def func2(x, y):
	return (1-y)**2+100*(x-y**2)**2
def grad2(x, y):
	return (200*(x-y**2), 2*(-200*x*y+200*y**3+y-1))
def func1(x):
	return (x-1)**2
def func(x,y):
	return 4* x**2-3*x*y+2*y**2+24*x-20*y
def grad(x, y):
	return (8*x-3*y+24, 4*(y-5)-3*x)
def min_f(func, grad, error, lam):
	x = 2
	y= 2
	iters = 0
	# p = lambda lam: func(x - lam*grad(x,y)[0], y - lam*grad(x,y)[1])
	# lam = find_min(p, 0, 100, .0000001)
	while((math.sqrt(grad(x,y)[0]**2 +grad(x,y)[1]**2))**2)>error:
		iters += 1
		x -= lam*grad(x,y)[0]
		y -= lam*grad(x,y)[1]
	return x,y, iters

#print(find_min(func1, -3, 3, .000000000001))
lam = 0.01
iters = []
lams = []
while lam <= .3:
	lams.append(lam)
	iters.append(min_f(func, grad, .000000001, lam)[2])
	lam+= .01
plt.plot(lams, iters)
plt.show()
# print(min_f(func, grad, 0.000000001, 0.1))
# print(min_f(func2, grad2, 0.000000001, 0.1))

# while previous_step_size > precision:
# 	prev_x = x
# 	x += -step_rate*grad_desc(prev_x)
# 	previous_step_size = abs(x - prev_x)
# print("The local minimum occurs at %f" % cur_x)