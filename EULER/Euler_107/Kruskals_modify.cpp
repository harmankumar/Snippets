#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<limits>
#include<queue>
#include<set>
using namespace std;

const int size=40;
const int inf=numeric_limits<int>::max();

struct uf
{
	//int num;
	int parent;
	int size;
	
	uf()
	{
	//	num=0;
		parent=0;
		size=1;		
	}
};

struct node
{
	int val;
	int x;
	int y;
};

struct mycomp
{
	bool operator() (const node & a1, const node & a2) const
	{
		return a1.val>a2.val;
	}	
};


int main()
{
	uf myuf[size];
	for(int i=0;i<size;i++)
	{
		myuf[i].parent=i;
	}
	priority_queue<node,vector<node>,mycomp> mypq;
	set<int> s;
	long long tot_sum=0;
	ifstream f;
	f.open("modify.txt");
	int a[size][size];
	char x;
	for(int i=0;i<size;i++)
		for(int j=0;j<size;j++)
			{
				f>>a[i][j];
				f>>x;
			}
			node n;
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<=i;j++)
			{
				tot_sum+=a[i][j];
				
				n.x=i;
				n.y=j;
				if(a[i][j]==0)
					a[i][j]=inf;
	//			cout<<a[i][j]<<" ";
				n.val=a[i][j];
				mypq.push(n);
			}
	//	cout<<endl;
	}
	long long mincost=0;
	int count=0;
	while(count!=size-1)
	{
		node temp=mypq.top();
		mypq.pop();
		if(myuf[(temp.x)].parent==myuf[(temp.y)].parent)
			continue;
		else
		{
			cout<<temp.x<<" "<<temp.y<<" "<<temp.val<<endl;
		
			int val=myuf[(temp.x)].parent;
			int newval=myuf[(temp.y)].parent;
			for(int i=0;i<size;i++)
			{
				if(myuf[i].parent==val)
				{
					myuf[i].parent=newval;	
				}
			}
			
			//myuf[(temp.x)].parent=myuf[(temp.y)].parent;
			mincost+=temp.val;
			count++;
		}
	}
	
	cout<<s.size()<<" "<<count<<endl;
	cout<<tot_sum-mincost<<endl;
	
	


	return 0;
}
