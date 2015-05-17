#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
	int a[200][200]={0};
	int x,count=0;
	ifstream f;
	f.open("input.txt");
	while(!f.eof())
	{	//count++;
		for(int i=0;i<=count;i++)
		{
			f>>x;
			cout<<x<<" ";
			a[count][i]=x;
		}
		count++;
	}
	
	while(count>=0)
	{
		count--;
		for(int i=0;i<=count;i++)
		{
			if(a[count+1][i]>a[count+1][i+1])	a[count][i]+=a[count+1][i];
			else a[count][i]+=a[count+1][i+1];
		}
	}
	for(int i=0;i<100;i++)
	{
		for(int j=0;j<100;j++)
		cout<<a[i][j]<<" ";
		cout<<endl;
	}
	
	cout<<a[0][0];
	
	return 0;
}
