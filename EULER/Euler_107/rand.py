import math

val=math.pow(10,7)

def findprime(a,b):
		x=[0 for i in range(0,int(b+1))]
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

def totient(x):
	global val
	f=open("output.txt","w")
	z=87108
	while z<=val:
		z=z+1

		if z in x:
			continue
		
		else:
			l=[]
			for i in x :
				if(i>z):
					break
				if(z%i==0):
					l.append(i)
			prod=1.0
			#print  z, " ",l, " ",
			for i in l:
				prod=prod*float(1-float(1.0/i))

			prod=prod*z	
			#print prod,
			
			m=str(z)
			n=str(int(prod))
			m=list(m)
			n=list(n)
			k= str(z)+" "+str(int(prod))+"\n"
			if(len(m)==len(n)):
				m.sort()
				n.sort()	
				if(m==n):
					f.write(k)


		
	f.close()
	print "fin_done"
		
def main():
	x=findprime(0,int(val))
	print "DONE "
	totient(x)

	


if (__name__ == '__main__'):
	main()