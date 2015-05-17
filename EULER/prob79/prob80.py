import math

primelist=[]

def findprime(a,b):
		x=[0 for i in range(0,b+1)]
		x[0]=x[1]=1
		i=2
		while(i<math.sqrt(b)):
			count=2*i
			while(count<=b):
				x[count]=1
				count=count+i
			i=i+1
			while(x[i]!=0):
				i=i+1
	#	for i in range(0,b+1):
	#		if(x[i]==0):
	#			print i
		t=[]
		for i in range(a,b+1):
			if(x[i]==0):
				t.append(i)
		return t

def factors(n):
	ret_list=[]
	i=0
	while(n>1):
		if(n%primelist[i]==0):
			ret_list.append(primelist[i])
			while(n%primelist[i]==0):
				n=n/primelist[i]
		else:
			i=i+1
	return ret_list

def totient(n):
	if(n in primelist):
		return n-1

	faclist=factors(n)
	ret_val=n
	for i in faclist:
		ret_val=ret_val-ret_val/i
	return ret_val

def main():
	count=0
	global primelist
	primelist=findprime(0,1000000)
	
	truelist=[i for i in range(0,1000001)]
	truelist[1]=0
	for elem in primelist :
		temp_val=elem
		while(temp_val<1000001):
			truelist[temp_val]=truelist[temp_val]-truelist[temp_val]/elem
			temp_val=temp_val+elem

	for i in truelist:
		count=count+i
	print count


if __name__ == '__main__':
	main()