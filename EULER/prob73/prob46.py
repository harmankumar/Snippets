import math

sqlist=[]
prlist=[]

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

def check(n):
	for i in sqlist:
		if(i>n):
			break
		elif(n-i in prlist):
			return True
		elif(n-i==0):
			return True

	return False

def main():

	global prlist , sqlist
	prlist=findprime(0,1000000)
	i=1
	while(i<10000):
		sqlist.append(2*i*i)
		i=i+1

	print "Done"
	i=9
	while(1):
		if(i in prlist):
			i=i+2
		elif(check(i)==False):
			break
		else:
			i=i+2
			print i
	print i


if __name__ == '__main__':
	main()