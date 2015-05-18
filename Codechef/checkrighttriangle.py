import math

def isrighttriangle(x1,y1,x2,y2,x3,y3):
	diffx1 = x2-x1
	diffy1 = y2-y1
	diffx2 = x3-x2
	diffy2 = y3-y2
	diffx3 = x1-x3
	diffy3 = y1-y3

	if((diffy1*diffy2 + diffx1*diffx2 == 0) or (diffy2*diffy3 + diffx2*diffx3 == 0) or (diffy3*diffy1 + diffx3*diffx1 == 0)):
		return True
	else:
		return False

def main():
	t = raw_input()
	t = int(t)
	count = 0
	for i in range(0,t):
		x = raw_input()
		x = x.split()
		x1 = int(x[0])
		y1 = int(x[1])
		x2 = int(x[2])
		y2 = int(x[3])
		x3 = int(x[4])
		y3 = int(x[5])
		if(isrighttriangle(x1,y1,x2,y2,x3,y3)):
			count += 1
	print count 

if __name__ == '__main__':
	main()