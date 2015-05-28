#include<iostream>
#include<queue>
#include<string>
#include<vector>
#include<map>
#include<stdio.h>

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
	
	map <string, int> mymap;
	
	mymap.insert(make_pair("Harman",1));
	mymap.insert(make_pair("Is",2));
	
	pair<int,int> test;
	
	test.first=10;
	test.second=20;
	
//	cout<<test.first<<endl<<test.second<<endl;
	
/*	
	map<string,int>::iterator it;
	for(it=mymap.begin();it!=mymap.end();it++)
		cout<<((*it).first)<<" "<<(*it).second<<endl;
		
	cout<<mymap.count("Automobile")<<endl;
	cout<<mymap.size();
*/
	priority_queue<int,vector<int>,Lessthan> mypq;
	
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
