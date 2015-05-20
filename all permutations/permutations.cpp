#include <iostream>
#include <fstream>

using namespace std;

void display(int a[],int size)
{
	for(int i=0;i<size;i++)
		cout<<a[i]<<" ";
	
	cout<<endl;
}

void swap(int& a,int& b)
{
	int t=a;
	a=b;
	b=t;
}

void permute(int a[],int index,int size)
{
	if(index==size-1)
	{
		display(a,size);
	}

	else
	{
		for(int i=index;i<size;i++)
		{
			swap(a[i],a[index]);
			permute(a,index+1,size);
			//cout<<"testing: ";
			//display(a,size);
			swap(a[i],a[index]);
		}
	}

}

int main()
{
	int size;
	
	cin>>size;

	int *arr = new int[size];

	for(int i=0;i<size;i++)
		cin>>arr[i];

	permute(arr,0,size);

	return 0;
}