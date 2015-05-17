import math



def main():
	N=raw_input()
	N=int(N)
	while(N):
		x=raw_input()
		x=x.split()
		s=int(x[0])
		a=int(x[1])
		b=int(x[2])
		c=int(x[3])
		sum=0
		for i in range(0,a+1):
			if i>s:
				break
			temp=s-i
			
			if((temp<=b)and(temp<=c)):
				sum=sum+((temp+2)*(temp+1)/2)
			
			elif((temp>b)and (temp<=c)):
				sum=sum+((temp+2)*(temp+1)/2)
				sum=sum-((temp-b)*(temp-b+1)/2)
			
			elif((temp>c)and (temp<=b)):
				sum=sum+((temp+1)*(temp+2)/2)
				sum=sum-((temp-c)*(temp-c+1)/2)
			
			elif((temp>b)and(temp>c)):
				
				if(b+c>temp):
					sum=sum+((temp+1)*(temp+2)/2)
					sum=sum-((temp-c)*(temp-c+1)/2)
					sum=sum-((temp-b)*(temp-b+1)/2)
			
				if(b+c==temp):
					#sum=sum+((temp+1)*(temp+2)/2)
					#sum=sum-((temp-c)*(temp-c+1)/2)
					#sum=sum-((temp-b)*(temp-b+1)/2)
					#sum=sum-1
					sum=sum+((b+1)*(c+1))

				else:
					sum=sum+((temp+1)*(temp+2)/2)
					sum=sum-((temp-c)*(temp-c+1)/2)
					sum=sum-((temp-b)*(temp-b+1)/2)
					sum=sum+((temp-a-b+1)*(temp-a-b+2)/2)
		print sum			

		N=N-1

if __name__ == "__main__":
	main()