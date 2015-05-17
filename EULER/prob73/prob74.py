import math

glolist=[]


def looping(n):
	global glolist
	mylist=[]
	temp=n
	while(1):
		if temp in mylist:
			break
		if(temp<n):
			return len(mylist)+glolist[temp]
			break
		mylist.append(temp)
		mystr=str(temp)
		mystr=list(mystr)
		sum=0
		for i in mystr:
			sum=sum+math.factorial(int(i))
		temp=sum
		#mylist.append(sum)	
	return len(mylist)

def main():
	count=0
	global glolist
	glolist.append(0)
	for i in range (1,1000000):
		mynum=looping(i)
		if mynum==60:
			count=count+1
		glolist.append(mynum)
	print count
if __name__ == '__main__':
	main()