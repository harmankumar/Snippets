import math

def digsum(l):
	mysum=0
	for i in l:
		mysum=mysum+i
	return mysum

def main():
	maxsum=0
	for i in range(1,100):
		myli=[0 for k in range(0,300)]
		#print myli

		if(i%10!=0):

			myli[298]=i/10
			myli[299]=i%10
			count=0
			while(count<99):
				tempres=digsum(myli)
				if(i==99 and (count==1 or count==0)):
					print myli
				#print tempres
				if(tempres>maxsum):
					maxsum=tempres
					templist=[0 for t in range (0,300)]
				for j in range(0,300):
					templist[j]=myli[j]*i
				myli=[0 for k in range(0,300)]
				if(i==99 and (count==1 or count==0)):
					print templist
				for j in range(1,300):
					myli[300-j-2]=myli[300-j-2]+(templist[300-j]/100)%10
					myli[300-j-1]=myli[300-j-1]+(templist[300-j]/10)%10
					myli[300-j]=myli[300-j]+templist[300-j]%10
				if(i==99 and (count==1 or count==0)):
					print myli				
				for j in range(1,300):
					myli[300-j-1]=myli[300-j-1]+myli[300-j]/10
					myli[300-j]=myli[300-j]%10	
				count=count+1
	print maxsum


if __name__ == '__main__':
	main()