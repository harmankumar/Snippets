#include <iostream>
#include <algorithm>


using namespace std;

int main()
{
	int t,arr[2000];
	cin>>t;
	while(t != 0)
	{
		int count = 0;
		for(int i=0;i<t;i++)
			cin>>arr[i];
		sort(arr , arr+t);

		for(int i=0;i<t-2;i++)
		{
			int k = i+2;

			for (int j = i+1; j < t-1; ++j)
			{
				while(arr[i]+arr[j] >= arr[k] && k<t)
				{
					k++;
				}	
				count += t-k;
			}
		}

		cout<<count<<endl;
		cin>>t;

	}
	return 0;
}