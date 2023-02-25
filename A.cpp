#include<bits/stdc++.h>
#define ll long long 
#define vi vector<int>
#define f first
#define s second
using namespace std;
bool check_func(vector<ll>& A,vector<ll>& B,ll m,ll k){
	ll S=0;
	for(int i=0;i<A.size();++i){
		S+=max(0ll,(m*A[i]-B[i]));
	}
	if(S<=k) return true;
	return false;
}
void test_case(){
	int n;
	cin>>n;
	cout<<(3<<n)<<"\n";

	
}
int main(){
	int T=1;
	//scanf("%d",&T);
	while(T--) test_case();
	
}