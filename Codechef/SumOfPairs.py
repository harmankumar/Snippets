
hashtable = {}
arr = []
t = 0
maxinhash = 0

def hashmap(n):
	global hashtable
	global arr
	global t
	global maxinhash
	
	i = 0
	j = t-1
	count = 0

	while j > i :
		if(arr[i] + arr[j] == n):
			count += 1
			i += 1
			j -= 1
		if(arr[i] + arr[j] > n):
			j -= 1
		if(arr[i] + arr[j] < n):
			i += 1

	hashtable[n] = count

	if(count > maxinhash):
		maxinhash = count


t = int(raw_input())

arr = raw_input()
myset = []
if t <= 1 :
	print 0

else:

	arr = arr.split()
	arr = map(int , arr)
	arr.sort()
	for i in range(t-1):
		for j in range(i+1,t):
			myset.append(arr[i]+arr[j])
	myset = list(set(myset))
	for k in myset:
		hashmap(k)

	print 2*maxinhash

