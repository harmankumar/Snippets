#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <fstream>
using namespace std;

void swap(int& a, int& b)
{
	int t=a;
	a=b;
	b=t;
}

int main()
{
	ifstream f;
	f.open("read.txt");

	int size;
	f>>size;

	int * arr = new int[size];
	int i=0;

	while(f)
	
		f>>arr[i++];

	for(i=0;i<size;i++)
	{
		int x = rand()%(i+1);
		swap(arr[i],arr[x]);
	}	
	f.close();

	ofstream f1;
	f1.open("write.txt");

		f1<<size<<endl;
	for(int i=0;i<size;i++)
	{
		f1<<arr[i]<<endl;
	}
	f1.close();
	return 0;
}