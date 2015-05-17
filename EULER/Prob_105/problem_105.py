


def check(n):
	


def main():
	f=open("input.txt")

	sum=0

	for i in f:
		x=i.split(",")
		arr=[]
		for j in x:
			if("\n" in j):
				arr.append(int(j.replace("\n","")))
			else:
				arr.append(int(j))	
		if(check(arr)==True):
			for i in arr:
				sum=sum+i

	f.close()


if __name__ == '__main__':
	main()