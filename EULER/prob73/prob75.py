import math

mybignum=1500001

def gcd(a,b):
	if(b==0):
		return a
	else: 
		return gcd(b,a%b)

def main():
	counting=0
	global mybignum
	mylist=[0 for i in range(0,mybignum)]
	myrange=math.sqrt(mybignum)
	for i in range(1,int(math.floor(myrange))):
		for j in range (1,i):
			if((gcd(i,j)==1) and ((i+j)%2==1)):
				mysum=2*i*(i+j)
				tempno=mysum
				while(tempno<mybignum):
					mylist[tempno]=mylist[tempno]+1
					tempno=tempno+mysum

	count=0
	print counting
	for i in mylist:
		if(i==1):
			count=count+1
	print count
	print mylist[120]
	#print int(1.0)==1.0


if __name__ == '__main__':
	main()