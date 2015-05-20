#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream f;
	f.open("input.txt");
	int size;
	f>>size;
	int **a= new int* [size];
	for(int i=0;i<size;i++)
	{
		a[i]=new int[size];
	}

	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			f>>a[i][j];
		}
	}
	f.close();

	for(int i=size-1;i>0;i-=2)
	{
		int row1=size-i-1;
		int row2=i;
		int col1=row1;
		int col2=row2;

		for(int j=0;j<i;j++)
		{
			int temp1=a[row1][col1+j];
			int temp2=a[row1+j][col2];
			int temp3=a[row2][col2-j];
			int temp4=a[row2-j][col1];
			a[row1][col1+j]=temp4;
			a[row1+j][col2]=temp1;
			a[row2][col2-j]=temp2;
			a[row2-j][col1]=temp3;
		}
	}

	ofstream f1;
	f1.open("output.txt");
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			f1<<a[i][j]<<" ";
		}
		f1<<endl;
	}

}