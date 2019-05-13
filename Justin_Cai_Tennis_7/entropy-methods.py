import math
import csv
def data():
    ds=[]
    dn=[]
    title=None
    with open('house_votes.csv','r') as csvfile:
        readerx = csv.reader(csvfile)
        for r in readerx:
            if title==None:
                title=r[1:-1]
            else:
                if not "?" in r[1:]:
                    ds.append(r[1:])
                else:
                    dn.append(r[1:])
    return dn,ds,title
def make_tree(ds,level,title,tree):
    best_col,num=best(ds)
    #print("---"*level,title[num],"-")
    s=set(best_col)
    for val in s:
        new_ds,nt=extract(ds,num,val,title)
        if len(set(answers(new_ds)))==1:
            #print("---"*level+">",val,answer(new_ds))
            tree.append([title[num],val,str(list(answer(new_ds).keys())[0])])
        else:
            #print("---"*level+"> "+val,"...",answer(new_ds))
            tree.append([title[num],val])
            make_tree(new_ds,level+1,nt,tree)
            
    return tree
def answers(ds):
    a=[]
    for x in ds:
        a.append(x[-1])
    return a
def answer(ds):
    a=[x[-1] for x in ds]
    freq={x: a.count(x) for x in set(a)}
    return freq
def extract(ds,num,val,title):
    new=[]
    nt=list(title[0:num]+title[num+1:])
    for x in ds:
        if x[num]==val:
            new.append(x[0:num]+x[num+1:])
    return new,nt
def best(ds):
    result=[]
    bestcol=None
    b=1000
    for z in ds:
        result.append(z[len(z)-1])
    for y in range(len(ds[0])-1):
        dictcol={}
        row=0
        array=[]
        for x in ds:
            r=x[y]
            if not(r in dictcol.keys()):
                dictcol[r]=[result[row]]
            else:
                dictcol[r].append(result[row])
            row=row+1
        for x in dictcol:
            array.append(list(answer(dictcol[x]).values()))
        if avg_entropy(array)<b:
            b=avg_entropy(array)
            bestcol=y
    best_col=[]
    for x in ds:
        best_col.append(x[bestcol])
    return best_col,bestcol
def entropy(x):
    total = 0
    totale=0
    for d in x:
        total=d+total
    for d in x:
        if d != 0:
            totale=totale+((d/total)*(-(math.log(d/total)/math.log(2))))
    return totale
def avg_entropy(x):
    s=0
    total=0
    for e in x:
        smallsum=0
        for y in e:
            total=y+total
            smallsum=smallsum+y
        s=s+entropy(e)*(smallsum)
    return s/total
def makedecision(x,title,tree):
    case=None
    for y in tree:
        if case==None:
            case=y[0]
        if x[title.index(y[0])]==y[1] and case==y[0]:
            if len(y)==3:
                return y[2]
            else:
                case=None
    return "miss"
def calc_accuracy(dn,title,tree):
    c=0
    wrong=0
    for x in dn:
        print(x)
        r=makedecision(x[:-1],title,tree)
        if r==x[-1]:
            c=c+1
    return c/len(dn)
import random
dn,ds,title=data()
tree = make_tree(ds, 1, title, [])
calc_accuracy(dn, title, tree)
#print(make_tree(ds, 1, title, []))
##xaxis=[]  
##yaxis=[[] for i in range(200)]
##zaxis = [[] for i in range(200)]
##for x in range(10,200):
##    for y in range(100):
##        random.shuffle(ds)
##        xaxis.append(x)
##        
##        tree=make_tree(ds[0:x],1,title,[])
##        print(tree)
##        for node in tree:
##            yaxis[x].append(len(tree))
##        zaxis[x].append(calc_accuracy(dn, title, tree))
     #   print(calc_accuracy(dn,title,tree))
 #   print(sum(zaxis[x])/100)
##import matplotlib.pyplot as plt
##plt.plot(xaxis,yaxis)
##plt.show()

