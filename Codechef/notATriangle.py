import math

def istriangle(a,b,c):
	if( a+b < c or a+c < b or b+c < a):
		return True

	return False

def main():

	n = raw_input()
	n = int(n)
	
	while n != 0:
		count = 0
		arr = raw_input()
		arr = arr.split()
		arr = map(int , arr)
		arr.sort()
		#print arr

		if n >= 3 :	
			for i in range (0,n-2) :
				for j in range(i+1,n-1):
					for k in range(j+1,n):
						if(istriangle(arr[i],arr[j],arr[k])):
							count = count + n-k
							break
						
			print count
		
		else :
			print 0

		n = raw_input()
		n = int(n)

if __name__ == '__main__':
	main()