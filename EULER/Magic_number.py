import math

def main():

	adj_list = [[] for x in range(200)]

	f=open("input.txt")
	i=0
	for line in f:
		
		#print line
		j=line.split()
		print i, " ", j
		for x in j:
			adj_list[i].append(int(x))
		i=i+1

		for i in range (0,200):
			adj_list[i].remove(i+1)
			print i

	for i in range (0,200):
		print i, ":  ", adj_list[i]
if __name__ == '__main__':
	main()