#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>

using namespace std;

const long long size=100000;

vector<int>* prime_fac(int n)
{
	vector<int>* temp = new vector<int>;
	
	int gc=2;
	while(n!=1)
	{
		if(n%gc==0)
		{
			temp->push_back(gc);
			n/=gc;
		}
		
		else
		{
			gc++;
		}
	}
	
	return temp;
}

int gcd(int a, int b)
{
	if(a<b)
	{
		int temp=b;
		b=a;
		a=temp;
	}
	
	if(b==0)	return a;
	
	else	return gcd(b,a%b);
}

long long lcm(int a, int b)
{
	int temp=gcd(a,b);
	return a*b/temp;
}

int main()
{

	ofstream f;
	f.open("q108.txt");
	int* arr=new int[size+1];
	for(int ter=0;ter<size+1;ter++)
		arr[ter]=0; 
	vector<int>* temp;
	vector<int>::iterator it;
	
	//temp=prime_fac(90);
	
	//for(it=temp->begin();it!=temp->end();it++)
	//	cout<<*it<<endl;
	
	long long i,j;
	i=2;
	while(i<=size)
	{
		j=1;
		while(j<=i/2)
		{
			if(gcd(j,i-j)==1)
			{
				long long lc=lcm(j,i-j);
				long long lc1=lc;
				while(lc<=size)
				{
					arr[lc]++;
					lc+=lc1;
				}
			}
			
			j++;
		}
		
		i++;
	}
	
	for(i=0;i<=size;i++)
	{
	//	f<<i<<" "<<arr[i]<<endl;
		if(arr[i]>1000)	cout<<i<<endl;
	}
	
	return 0;
	
}
