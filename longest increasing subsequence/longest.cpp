#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define F(i,size) for(i=0;i<size;i++);

struct node
{
	int val=0;
	vector<int> vec;
};


int main()
{
	
	vector<int> :: iterator it,it1;
	int size;
	ifstream f;
	f.open("read.txt");
	f>>size;
	int *a=new int[size];
	int i,j;
	for(i=0;i<size;i++)
	f>>a[i];

	//cout<<size<<endl;
	node* store= new node[size];

	for(i=0;i<size;i++)
	{
		store[i].val=1;
		(store[i].vec).push_back(a[i]);

		//cout<<a[i]<<" *"<<endl;
	}
	
	//for(i=0;i<size;i++)
	//{
	//	cout<<(store[i].vec)[0];
	//}
	
	for(i=0;i<size;i++)
	{
		int max=0;
		int temp=-1;
		for(j=0;j<i;j++)
		{
			if(a[i]>a[j])
			{
				if(store[j].val>max)
					{
						max=store[j].val;
						temp=j;
					}
			}
		}
			if(temp>-1)
			{
				store[i].val += max;
				it=(store[temp].vec).end();
				it--;
				for(;it>=store[temp].vec.begin();it--)
				{
					it1=store[i].vec.begin();
					(store[i].vec).insert(it1,*it);
				}
			}
			//cout<<store[i].val<<endl;
	}
	int max=0;
	
	for(i=0;i<size;i++)
	{	
		cout<<store[i].val<<"    ";
		for(it=(store[i].vec).begin();it<(store[i].vec).end();it++)
		{
			cout<<*it<<" ";
		}	
		cout<<endl;
	}

	

	return 0; 

}
