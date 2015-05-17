import math

def isprime(n):
	if(n<2):
		return False
	temp=math.sqrt(n)
	for i in range(2,int(temp)):
		if(n%i==0):
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
	#mylist=findprime(0,10000000)
	#print "Done"
	i=3
	j=0
	diag1=0
	diag2=0
	num1=1
	num2=1
	tempnum=2
	
	while(1):
		num1=num1+4*i-8
	#	print num1
		if(isprime(num1)):
			diag1=diag1+1
		for k in range(0,2):	
			num2=num2+tempnum
			tempnum=tempnum+2
			if(isprime(num2)==True):
				diag1=diag1+1
		myratio=float(diag1)/float(2*i-1)
	
		if(myratio<0.1):
			break
		else:
		#	print "inelse",
			i=i+2
		#	print myratio," ", i , ' ', diag1," ", diag2
		if(i>26000):
			print "Yes", myratio
	print i


if __name__ == '__main__':
	main()