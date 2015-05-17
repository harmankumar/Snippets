import math
import sets

maxval=math.pow(10,10)
minval=math.pow(10,9)

def checkpan(n):
	if(len(n)<9):
		return False
	n=list(n)
	for i in range (1,len(n)+1):
		if(str(i) in n):
			continue
		else:
			return False
	return True

def main():
	myset=set()

	for i in range(1,10000):
		if(i%1000==0):
			print i
		minv=minval/i
		maxv=maxval/i
	#	if((i<minv) or (i>maxv)):
	#		continue
	#	else:
		if(True):
			for j in range(1,i):
				prod=i*j
				tempstr=str(int(i))+str(int(j))+str(prod)
				if(checkpan(tempstr)==True):
					myset.add(prod)
	
	count=0
	for i in myset:
		count=count+i
	print count
if __name__ == '__main__':
	main()