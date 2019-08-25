import math
import numpy
count = len(open("p2.txt").readlines(  ))
f2=open("p2.txt", "r")
c = 1
fl =f2.readlines()
for l in fl:
    if c == 1:    	
    	T,n = l.split(" ")
    	T=int(T)
    	n=int(n)
    if c == 2:
    	x = l.split(" ")
    	x = [float(i) for i in x] 
    if c == 3:
    	y = l.split(" ")
    	y = [int(i) for i in y] 
    if c == 4:
    	p = l.split(" ")
    	p = [float(i) for i in p] 
    c +=1

f=[0]*n
E_b=1
for i in range(T):
	print('============ Run : ' +str(i)+ ' =============')
	print('')
	e=[]
	d={}
	p_n=[None] * n
	z=0
	
	for j in range(n-1):
		a=(x[j] + x[j+1])/2

		for k in range(2):
			if k == 0:
				
				d['I( x < '+str(a) +' )']=[]
				y_exp = [1 for p in range(j+1)]
				y_exp.extend([-1 for p in range(j,len(y)-1)]) 
				g=0
				for h in range(len(y)):
					if y[h] != y_exp[h]:
						g+=p[h]
						d['I( x < '+str(a) +' )'].append(h)

				e.append(g)	

			if k == 1:
				d['I( x > '+str(a) +' )']=[]
				y_exp = [-1 for p in range(j+1)]
				y_exp.extend([1 for p in range(j,len(y)-1)]) 
				g=0
				for h in range(len(y)):
					if y[h] != y_exp[h]:
						g+=p[h]
						d['I( x > '+str(a) +' )'].append(h)
				e.append(g)
	
	r=e.index(min(e))
	er = min(e)
	print('The weak classifier ht :' ,list(d.items())[r][0])
	print('The error of ht: ' ,er)
	alpha = 0.5 * math.log((1-er)/er)
	print('The weight of the weak classifier (Alpha) is ',alpha)
	
	d1 = list(d.items())
	p3 = list(d.items())[r][1] #incorrectly classified

	for u in range(n):
		if u in p3:
			p_n[u] = math.exp(alpha)
		else:
			p_n[u] = math.exp(-alpha)

	for q in range(n):
		z += p[q]*p_n[q]
	print('The probability normalization factor Zt: ',z)
	E_b *= z
	for w in range(n):
		p[w]= (p[w]*p_n[w])/z

	print('The probabilities after normalization:  ',p)
	o = list(d.items())[r][0].split(" ")
	sig = o[2]
	val = o[3]

	for v in range(n):
		if sig == '>':
			if x[v] > float(val):
				f3 = f[v] + alpha
				f[v] = f3
			else:
				f3 = f[v] - alpha
				f[v] = f3
		elif sig == '<':
			if x[v] < float(val):
				f3 = f[v] + alpha
				f[v] = f3
			else:
				f3 = f[v] - alpha
				f[v] = f3

	print('The boosted classifier: ft.: ',f)
	zz = 0
	oo=[0] * n 
	for qw in range(n):
		if f[qw] < 0:
			oo[qw] = -1
			
		else:
			oo[qw] = 1

	for we in range(n):
		if oo[we] != y[we]:
			zz += 1
	
	
	err_b = zz/n
	print('The error of the boosted classifer: Et.' , err_b)
	print('The bound on Et:',E_b)
	print('')


