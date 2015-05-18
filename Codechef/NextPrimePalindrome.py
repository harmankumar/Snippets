import math

def isprime(n):
	temp = long(math.sqrt(n)+1)
	for i in range(2,temp):
		if(n%i == 0):
			return False
	return True

def checkpal(n):
	if(len(n) == 1):
		return True
	if(len(n) == 2):
		return n[0] == n[1]
	if(n[0] == n[len(n)-1]):
		return checkpal(n[1:-1])

def main():
	n = raw_input()
	n = int(n)
	if(n%2 == 0):
		n=n+1
	while (1):
		if(checkpal(str(n))):
			if(isprime(n)):
				print n
				break
		n += 2
if __name__ == '__main__':
	main()