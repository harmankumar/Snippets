import math
from fractions import Fraction

def sumofdig(n):
	n=str(n)
	i=0
	count=0
	while(i<len(n)):
		count=count+int(n[i])
	return count

def check(i):
	buf=1
	nano=1
	while(nano<=math.pow(10,i)):
		nano=nano*i
		if(sumofdig(nano)==i):
			return True
		buf=buf+1
		
	return False


	return False	
def main():
	count=0
	i=1
	while count<40:
		if(check(i)==True):
			print i
			count=count+1
		i=i+1

	#print Fraction(0.3333).limit_denominator()


if __name__ == "__main__":
	main()