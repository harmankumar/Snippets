#include <cstdio>

using namespace std;

int main()
{
	long long t,q,testnum;
	scanf("%lld" , &t);
	scanf("%lld" , &q);
	long long count = 0;

	while(t--)
	{
		scanf("%lld" , &testnum);
		if(testnum%q == 0)
			count++;
	}

	printf("%d", count);
	return 0;
}