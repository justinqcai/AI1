import percy as p
import Perceptron as f

ar = f.cre()
#print(ar)
testor = [0, 1, 1, 0]
testnor = [1, 0, 0, 1]
finalout = []
count = 0
#print(ar)
for x in range(len(ar)):
	for y in range(len(ar)):
		for z in range(len(ar)):
			n1 = p.percy(ar[x], 0)
			n2 = p.percy(ar[y], 0)
			n3 = p.percy(ar[z], 0)
			n3.set_input([n1, n2, 1])
			xor = n3
			out = []
			for a in range(2):
				for b in range(2):
					n1.set_input([a,b,1])
					n2.set_input([a,b,1])
					out.append(int(xor))
			#print(out)
					#print(a, b, int(xor))
			if out == testor:
				#print(x, y, z)
				bo = True
				for it in finalout:
					if it[0] is y and it[1] is x and it[2] is z:
						bo = False
						break
				if bo:
					finalout.append([x, y, z])
					print(x, y, z)
					count+= 1

print(str(count) + " solutions")