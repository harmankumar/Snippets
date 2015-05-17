import math

def main():
	x=raw_input()
	x=x.split()
	n=int(x[0])
	q=int(x[1])

	arr1=[0 for x in range (n+1)] 
	arr2=[0 for x in range(n+1)]

	while(q):

		x = raw_input()
		x=x.split()

		if(x[0]=="RowAdd"):
			point=int (x[1])
			value=int(x[2])
			arr1[point]=arr1[point]+value
		else:
			point=int (x[1])
			value=int(x[2])
			arr2[point]=arr2[point]+value

		q=q-1

		max_row=max(arr1)
		print "Maxm in Row is ", max_row
		max_col=max(arr2)
		print "Maxm in column is ", max_col

	print max_col+max_row


if __name__ == "__main__":
	main()