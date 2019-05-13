from __future__ import division
import numpy as np
import math
import csv
import random
from random import shuffle
global headers
global CLASS_idx

class Node():
	def __init__(self, value, level):
		self.value = value
		self.children = []
		self.level = level
		self.answers = []
		self.ans = ""
		self.pruned = False
		self.parent = None
	def __str__(self):
		fnl = "\n" + "---"* self.level + self.value
		if len(self.ans) != 0:
			fnl+= "... " + self.ans
		if len(self.children) != 0:
			for i in self.children:
				fnl += i.__str__()
		return fnl
	def nodecount(self):
		if len(self.children) is 0:
			return 1
		else:
			count = 0
			for i in self.children:
				count += i.nodecount()
		return count
	def totalcount(self):
		if len(self.children) is 0:
			return 1
		else:
			if self.level is 0 or self.level%2 != 0:
				count = 1
				for i in self.children:
					count += i.totalcount()
			else:
				count = 0
				for i in self.children:
					count += i.totalcount()
		return count
	def getlevel(self, level, fnl):
		if self.level is level:
			fnl.append(self)
		else:
			for i in self.children:
				i.getlevel(level, fnl)
		return fnl
def spe_cre(size, lim):
	global headers
	global CLASS_idx
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
	headers = [str(x) for x in range(1, size+2)]
	CLASS_idx = len(headers)-1
	ds = {}
	count = 1
	for x in training:
		temp = x[0]
		temp.append(x[1])
		ds[count] = temp
		count += 1
	return ds, headers
def special_set(num, size):
	training = []
	ar = str(dec_to_bin(num, size))
	temp1 = []
	for y in ar:
		temp1.append(y)
	freq = {temp1.count(a): a for a in set(temp1)}
	out = freq[max(freq)]
	training.append(temp1)
	training.append(out)
	return training
def dec_to_bin(num, length):	
	return ("{:0" + str(length) + "b}").format(num)
def get_data(file):
	global CLASS_idx
	global headers
	qs = {}
	ds = {}
	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		headers = next(reader)[1:]
		for row in reader:
			if '?' not in row:
				ds[row[0]]= row[1:]
			else:
				qs[row[0]]= row[1:]
		csvfile.close()
	CLASS_idx = len(headers) - 1
	headers = headers
	return ds, qs, headers
def get_odd_data(file):
	global CLASS_idx
	global headers
	qs = {}
	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		headers = next(reader)[1:]
		for row in reader:
			if int(row[0]) %2 != 0:
				qs[row[0]]= row[1:]
		csvfile.close()
	CLASS_idx = len(headers) - 1
	headers = headers
	return qs, headers
def val_list(data, col):
	return [val[col] for val in data.values()]
def val_set(data, col):
	return set(val_list(data, col))
def restrict(data, col, val):
	return {a: data[a] for a in data if data[a][col] == val}
def freq_dist(data_dict):
	vals = val_list(data_dict, CLASS_idx)
	return {a: vals.count(a) for a in set(vals)}
def freq_entropy(freq_dict):
	f = list(freq_dict.values())
	s = sum(f)
	p=[i/s for i in f]
	return (-sum([i* math.log(i,2) for i in p if i>0]))
def parameter_entropy(data, col):
	length = len(data)
	total = 0
	for v in val_set(data, col):
		ds = restrict(data, col, v)
		l = len(ds)
		e = freq_entropy(freq_dist(ds))
		total += l/length * e
	return total
def make_tree(DS, level, node):
	col = best(DS)[1]
	#print("---"* level, headers[col], parameter_entropy(DS, col))
	if level is 1:
		node.value = headers[col]
		node.answers = answers(DS, col)
	else:
		temp = Node(headers[col], node.level + 1)
		temp.parent = node
		temp.answers = answers(DS, col)
		node.children.append(temp)
		node = temp
	for v in val_set(DS, col):
		new_ds =restrict(DS, col, v)
		freqs = freq_dist(new_ds)
		ent = freq_entropy(freqs)
		if(ent < .001):
			#print("---" * level + ">", headers[col] + " ... " + v, ent, freqs)
			temp = Node(v, node.level + 1)
			temp.parent = node
			temp.ans = list(freqs)[0]
			node.children.append(temp)
			#node.value = v
		else:
			temp = Node(v, node.level + 1)
			temp.parent = node
			node.children.append(temp)
			#print("---"*level + ">", headers[col] + " ... " + v, ent, freqs)
			make_tree(new_ds, level+1, temp)
	return node
def answers(DS, col):
	answer = {}
	for v in val_set(DS, col):
		new_ds = restrict(DS, col, v)
		fd = freq_dist(new_ds)
		for x in fd:
			answer[v, x] = fd[x]
	return answer
def best(DS):
	initial_h = freq_entropy(freq_dist(DS))
	bestcol = max((initial_h-parameter_entropy(DS, i), i) for i in range(CLASS_idx))
	return bestcol
def makedecision(x,tree):
	case=None
	for y in tree:
		if y.pruned is False:
			if case == None:
				if y.level % 2 == 0:
					case = y.value
				else:
					case = y.parent.value
			if y.parent is not None:
				if y.level%2 != 0:
					col = headers.index(y.parent.value)
					if x[col]==y.value and case == y.parent.value:
						if len(y.ans) != 0:
							return y.ans, y
						else:
							case=None
					elif x[col] == '?' and case == y.parent.value:
						if len(y.ans) != 0:
							# temp = []
							# for v in y.parent.answers:
							# 	temp.append(y.parent.answers[v])
							# hi = [i for i, lol in enumerate(temp) if lol == max(y.parent.answers)[1]]
							# if len(hi) > 1:
							# 	print "hi"
							return max(y.parent.answers)[1], y
						else:
							case = None
			# else:
			# 	if x[headers.index(y.value)]==y.parent.value and case == y.value:
			# 		if len(y.ans) != 0:
			# 			return y.parent.value
			# 		else:
			# 			case=None
	return "miss"
def prune(tree, decision):
	ans = decision[0]
	node = decision[1]
	for y in tree:
		if y.parent == node.parent and len(y.ans) != 0 and y.ans != ans:
			prunehelp(y)
def prunehelp(node):
	node.pruned = True
	for x in node.children:
		prunehelp(x)

def calc_accuracy(dn, tree):
	c=0
	misclass = 0
	for x in dn:
		r=makedecision(dn[x],tree)
		if r[0] == dn[x][-1]:
			#prune(tree, r)
			c += 1
	return c/len(dn)
def nodelist(tree, nl):
	nl.append(tree)
	for i in tree.children:
		nodelist(i, nl)
	return nl

# ds, qs, headers = get_data("quizB_train.csv")
# qs = get_odd_data("quizB_test_B.csv")[0]
# node = make_tree(ds, 1, Node(None, 0))
# print(calc_accuracy(qs, nodelist(node, [])))

row=[]  
x = 10
#nodes=[[] for i in range(200)]
acc = []
#ds, headers = spe_cre(10, 20)
while x <= 100:
	ds, headers = spe_cre(10, x)
	qs = spe_cre(10, x)[0]
	tacc = []
	for y in range(50):
		keys = list(ds.keys())
		random.shuffle(keys)
		newds = {}
		for a in range(x):
			newds[keys[a]] = ds[keys[a]]
		
		tree=make_tree(newds, 1, Node(None, 0))
		nl = nodelist(tree, [])
		tacc.append(calc_accuracy(qs, nl))
		#print(tree)
		#nodes[x].append(tree.nodecount())
	row.append(x)
	x+=5
	acc.append(sum(tacc)/len(tacc))
import matplotlib.pyplot as plt
plt.plot(row, acc)
plt.show()