import math

def main():

	t = raw_input()
	lis = []
	for i in range(int(t)):
		x = int(raw_input())
		lis.append(x)
		
	lis.sort()

	for i in lis:
		print i

if __name__ == '__main__':
	main()