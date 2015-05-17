import math

sum=0

def checkprop(s):
	#print s
	if(int(s[1]+s[2]+s[3])%2==0):
		if(int(s[2]+s[3]+s[4])%3==0):
			if(int(s[3]+s[4]+s[5])%5==0):
				if(int(s[4]+s[5]+s[6])%7==0):
					if(int(s[5]+s[6]+s[7])%11==0):
						if(int(s[6]+s[7]+s[8])%13==0):
							if(int(s[7]+s[8]+s[9])%17==0):
								return True
	# return False


def permute(s,i):
	global sum
	if(i==10):	
		if(checkprop(s)==True):
			sum=sum+int(s)

		#print s
		#sum=sum+1

	for j in range(i,10):
		x=list(s)
		x[j]=s[i]
		x[i]=s[j]
		k=''.join(x)
		permute(k,i+1)




def main():

	mystr="0123456789"

	permute(mystr,0)
	print sum
	#print checkprop("1406357289")
	#print checkprop("0123456789")

if __name__ == '__main__':
	main()
