import math

k=1
mylist=[1]

def findfac(n):
	i=math.sqrt(n)
	retlist={}
	counter=2
	while(n!=1)
		if(n%counter==1):
			n=n/counter
			retlist.add(counter)
			counter=counter-1
		counter=counter+1
	retlist=list(retlist)
	return retlist

def calc(lis):
	iniprod=1
	for i in lis:
		inprod=inprod*i
	

def main():
	i=2
	while (k<10000):
		lis=findfac(i)
		calc(lis)

		i=i+1



if __name__ == '__main__':
	main()