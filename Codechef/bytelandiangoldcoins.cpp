#include<bits/stdc++.h>
using namespace std;

map<long long , long long> dp;

long long byte ( long long n )
{
	if(n == 1)
		return 1;
	if(dp.find(n) != dp.end())
	{
		return dp[n];
	}
	else
	{
		return dp[n] = max(n,(byte(n/2) + byte(n/3) + byte(n/4)));
	}
}
int main()
{
	long long t;
	while(cin>>t)
	{
		cout<<byte(t)<<endl;

	}

	return 0;
}