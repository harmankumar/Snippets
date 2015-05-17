#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

long long count_inversion=0;

void merge(int[],int,int,int);

void mergesort(int a[],int min,int max)
{
	if(max==min)
	{

	}
	else if(max==min+1)
	{
		if(a[max]<a[min])
			{
				int t=a[max];
				a[max]=a[min];
				a[min]=t;
				count_inversion++;
			}
	}

	else
	{
		int mid=(max+min)/2;
		mergesort(a,min,mid);
		mergesort(a,mid+1,max);
		merge(a,min,mid+1,max+1);
	}

}

void merge(int a[], int min, int mid, int max)
{
	int i=min,j=mid,count=0;

	int* buf=new int[max-min+1];

	while((i<mid)&&(j<max))
	{
		int left_sofar=mid-i;

		if(a[i]<a[j])
			buf[count++]=a[i++];

		else if(a[j]<a[i])
			{
				count_inversion+=left_sofar;
				buf[count++]=a[j++];
			}

		else
		{
			count_inversion+=left_sofar-1;
			buf[count++]=a[i++];
			buf[count++]=a[j++];
		}
	}

	while((j<max))
			buf[count++]=a[j++];

	while((i<mid))
			buf[count++]=a[i++];

	for(i=min,j=0;i<max;i++,j++)
			a[i]=buf[j];
}

int main()
{
	int n;
//	cout<<" enter the number of elements ";
	ifstream f;
	f.open("input.txt");
	f>>n;
	int *a=new int[n];

	for(int i=0;i<n;i++)
		f>>a[i];

	mergesort(a,0,n-1);
	ofstream f1;
	f1.open("output.txt");

		
	f1<<"The Number of Inversions are "<<count_inversion;
		f.close();
		f1.close();
	return 0;
}
