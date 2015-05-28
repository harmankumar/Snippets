### a+b+c = 0 ###

def main():

	arr = raw_input()
	arr = arr.split()
	arr = map(int,arr)
	n = len(arr)
	arr.sort()

	for i in range(0 , n-2):
		a = arr[i]
		start = i+1
		end = n-1
		while(start < end):
			b = arr[start]
			c = arr[end]
			if( a+b+c == 0):
				print a , " " , b , " " , c
				start = start +1 
				end = end -1 
			elif( a+b+c < 0):
				start = start+1
			else:
				end = end-1

if __name__ == '__main__':
	main()