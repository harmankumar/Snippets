import math



def findpow(a,b):
	prod=float(b)
	a=float(a)
	prod=prod*math.log(a)
	return prod


def main():
	f=open("input.txt",'r')
	max=0
	l_no=0
	count=1
	for line in f:
		line=line.split(',')
		a=line[0]
		b=line[1]
		if(findpow(a,b)>max):
			max=findpow(a,b)
			l_no=count
		count=count+1
	print l_no


if __name__ == '__main__':
	main()