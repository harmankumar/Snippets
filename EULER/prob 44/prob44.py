import math

def checkpentagonal(n):

	temp=math.sqrt(1.0+24.0*n)
	temp=temp+1
	temp=temp/6.0

	if(int(temp)==float(temp)):
		return True
	
	else: 
		return False


def main():
	pentlist=[]

	mynum=1

	while(1):
		tempno=mynum*(3*mynum-1)/2
		pentlist.append(tempno)
		for i in pentlist:
			if((checkpentagonal(tempno-i)==True) and (checkpentagonal(tempno+i)==True)):
				print tempno-i
		#print pentlist

		mynum=mynum+1


if __name__ == '__main__':
	main()