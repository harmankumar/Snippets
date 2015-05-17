import math

mylist=[]

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

def count(n):
	i=0
	j=1
	sum=mylist[i]
	while(sum != n):
		if(sum<n):
			sum=sum+mylist[j]
			j=j+1
		else:
			sum=sum-mylist[i]
			i=i+1

	return j-i


def main():
	global mylist
	mylist=findprime(0,1000000)
	print "Done.."
	myprime=0
	maxcount=0

	for i in mylist:
		if (count(i)>maxcount):
			myprime=i
			maxcount=count(i)
			print maxcount

	print myprime




if __name__ == '__main__':
	main()