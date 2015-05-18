import math


def main():
	t = raw_input()
	t = int(t)
	for i in range(0,t):
		len = raw_input()
		len = int(len)

		lis = raw_input()
		sumpl = 0
		lis = list(lis)
		print lis
		sumpl = lis.count('1')
		ans = (sumpl*(sumpl+1))/2
		print ans

if __name__ == '__main__':
	main()