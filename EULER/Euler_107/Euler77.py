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

my_li=[0,1]

def getnum(n,l):
	global my_li
	if(n<0): 
		return 0
	elif(n==0):
		return 1
	else:
		s=0
		for i in range(1,n):
			s=s+1+my_li[n-i]
		#	print n, " ",l
		my_li.append(s)
		if(s%1000000==0):
			return True
		else:
			return False

def main():
	
	#l=findprime(0,100000)
	#print l
	i=2
	for i in range (2,10):
		val=getnum(i,i)
		#print val
		if(val==True):
			print i
			break
		#i=i+1
	print my_li
if (__name__ == '__main__'):
	main()