import math

arr = []

def fillup(n):
	count = 0
	for i in range(0,n+1):
		if(i%2 != 0):
			arr.append(arr[i-1])
		if(i%2 == 0):
			if(i < 4):
				count = 0
				arr.append(0)
			if(i >= 4):
				count = count+1
				arr.append(arr[i-1] + count)

def main():
	t = raw_input()
	t=long(t)
	fillup(10000)
	for i in range(0,t):
		n=raw_input()
		n=long(n)
		print str(arr[n])

if __name__ == '__main__':
	main()