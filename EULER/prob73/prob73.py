import math

mylist=[]
mynum=0
def hcf(a,b):
	myfrac=float(a)/float(b)


def findnum(n):
	global mynum
	global mylist
	lower=n/3.0
	upper=n/2.0
	lower=math.ceil(lower)
	upper=math.floor(upper)

	for k in range (int(lower),int(upper)+1):
		temp_no=float(k)/float(n)
		if(temp_no in mylist):
			continue
		else:
			mylist.append(temp_no)
			mynum=mynum+1


def main():
	count=0
	for i in range(1,12001):
		findnum(i)
		if(i%500)==0:
			print "Done"
	print mynum-2


if __name__ == '__main__':
	main()