
DenominationList = []
min_den = 0
max_den = 0
num_den = 0
DPDict = {}

def count(n):

	global DenominationList
	global DPDict
	global min_den
	global max_den
	global num_den
	temlis = []
	if(n < min_den):
		DPDict[n] = -1

	elif( n in DenominationList):
		DPDict[n] = 1
	
	else:
		for i in DenominationList:
			if(n - i < 0):
				break
			elif(DPDict[n-i] == -1):
				continue
			else:
				temlis.append(DPDict[n-i])
		if(len(temlis) == 0):
			DPDict[n] = -1
		else:
			DPDict[n] = 1 + min(temlis)



def main():

	global DenominationList
	global DPDict
	DPDict[0] = 0
	# t is the number of denominations available
	t = int(raw_input())
	num_den = int(t)
	lis = raw_input()
	lis = lis.split()
	lis = map(int,lis)
	lis.sort()
	DenominationList = lis
	min_den = min(lis)
	max_den = max(lis)

	query = raw_input()
	for i in range(1,int(query)+1):
		count(i)

	print DPDict




if __name__ == '__main__':
	main()