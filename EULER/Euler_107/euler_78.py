import math

def findprime(a,b):
		x=[0 for i in range(0,b+1)]
		x[0]=x[1]=1
		i=2
		while(i<math.sqrt(b)):
			count=2*i
			while(count<=b):
				x[count]=1
				count=count+i
			i=i+1
			while(x[i]!=0):
				i=i+1
	#	for i in range(0,b+1):
	#		if(x[i]==0):
	#			print i
		t=[]
		for i in range(a,b+1):
			if(x[i]==0):
				t.append(i)
		return t

def getnum(n,l):
	if(n<0): 
		return 0
	elif(n==0):
		return 1
	else:
		s=0
		for i in l:
			s=s+getnum(n-i,l[:(l.index(i)+1)])
		#	print n, " ",l
		return s

def main():
	
	l=[]
	for i in range(1,1000000):
		l.append(i)

	for i in range(2,400):
		val=getnum(i,l)
		#print val
		if(val%5000==0):
			print i
			break
if (__name__ == '__main__'):
	main()