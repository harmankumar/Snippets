import math

def main():
	mylist=[]
	f=open("input.txt","r")
	f1=open("newfile","w")
	for i in f:
		j=i.split(',')
		for k in j:
			mylist.append(j)
	mynewlist=[]
#	for x in sorted(mylist):
#		mynewlist.append(x)

	
	


if __name__ == '__main__':
	main()