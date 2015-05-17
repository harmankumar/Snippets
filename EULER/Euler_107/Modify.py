import math
from fractions import gcd
import sys

def comp(a,b):
	if(a>=b):
		return a
	else:
		return b

size=40

def main():

	f=open("input.txt","r")
	f1=open("modify.txt","w")
	sum=0
	for i in f:
		x=i.split(",")
		for j in x:
			print j
			z=j.replace("-","0")
			f1.write(z)
			sum=sum+int(z)
			f1.write(",")
	print sum
#	print a

if __name__ == "__main__":
	main()