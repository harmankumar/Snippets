import math

def main():
	i=1
	count=0
	mylist=[]
	while(count!=13):
		temp=math.sqrt(5*i*i+1)
		if(math.floor(temp)==math.ceil(temp)):
			mylist.append(long(i*i+math.pow((temp-2*i),2)))
			print mylist
			count=count+1
		temp=math.sqrt(5*i*i-1)
		if(math.floor(temp)==math.ceil(temp)):
			mylist.append(long(i*i+math.pow((temp-2*i),2)))
			print mylist
			count=count+1
		i=i+1
	print mylist	
	mysum=-1
	for i in mylist:
		mysum=mysum+long(i)
	print long(mysum)
if __name__ == '__main__':
	main()