import math

mylist=[]

def checkpan(n):
	n=str(n)
	n=list(n)
	for i in range (1,len(n)+1):
		if(str(i) in n):
			continue
		else:
			return False
	return True

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


def main():
	global mylist
	mylist=findprime(0,10000000)
	max=0
	for i in mylist:
		if(checkpan(i)==True):
			max=i
			
	print max

if __name__ == '__main__':
	main()