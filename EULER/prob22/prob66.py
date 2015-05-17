import math


def calc(n):
	y=1
	l=math.sqrt(n)
	if(math.floor(l)==math.ceil(l)):
		return 0

	while(1):
		tempsqrt=l*y
		for x in range(int(math.floor(tempsqrt)),1+int(math.ceil(tempsqrt))):
			if(math.pow(x,2)==(n*math.pow(y,2)+1)):
				return x
				break
		y=y+1

def main():

	max=0
	maxval=0
	for i in range(1,1001):
		temp=calc(i)
		print temp
		if(temp>max):
			max=temp
			maxval=i
	print maxval

if __name__ == '__main__':
	main()