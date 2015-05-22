import math

def findzer(n):
	div = 5
	sumtillnow = 0
	while(1):
		temp = int(math.floor(n/float(div)))
#		print temp
		sumtillnow = sumtillnow + temp
		div *= 5
		if temp == 0:
			break
	print int(sumtillnow)

def main():
	t = raw_input()
	t = int(t)
	for i in range(0,t):
		n = raw_input()
		n = int(n)
		numzer = findzer(n)

if __name__ == '__main__':
	main()