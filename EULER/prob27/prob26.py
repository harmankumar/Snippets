import math

def finlen(n):
	mylist=[]
	count=1
	mynum=1
	while(mynum<n):
		mynum=mynum*10
	#print "done"
	
	while(1):
		impnum=mynum%n
		#print impnum," ",n," ",mynum
		if(impnum in mylist):
			break
		elif(impnum==0):
			count=0
			break
		else :	
			count=count+1
			mylist.append(impnum)
			mynum=impnum
			mynum=mynum*10
			while(mynum<n):
				mynum=mynum*10
				count=count+1

	return count



def main():
	max=0
	maxnum=0

	for i in range (2,1001):
		temp=finlen(i)
		print temp
		if(temp>max):
			max=temp
			maxnum=i
	print maxnum


if __name__ == '__main__':
	main()