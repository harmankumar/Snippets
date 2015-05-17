#include<iostream>
#include<queue>
#include<string>

using namespace std;

struct Lessthan
{
	bool operator() (const int& a1, const int& a2) const
	{
		return a1>a2;
	}	
};

int main()
{
	priority_queue<int, vector<int>,Lessthan> mypq;
	mypq.push(5);
	mypq.push(425);
	mypq.push(56);
	mypq.push(545);
	mypq.push(55);
	
	while(!mypq.empty())
	{
		cout<<mypq.top()<<endl;
		mypq.pop();
	}
	
	return 0;
}
