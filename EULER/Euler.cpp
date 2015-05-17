#include<iostream>

using namespace std;

int cyclic(int a, int pow)
{ 
	

}

int main()
{
	int a[20]={2,3,5,7,11,13,17,19,23};
	int prod=1,i=0;
	while(prod<1000000)
	{	
		prod*=a[i++];
		cout<<a[i]<<" ";
	}
	cout<<prod<<endl;;
	i--;
	prod/=a[i];
	cout<<a[i]<<endl;;
	cout<<prod<<endl;
	
}
