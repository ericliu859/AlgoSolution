#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int main(){
	int t,n,i;
	long long m,p[8];
	cin >> t;
	while(t--){
		cin >> n >> m;
		for(i=0;i<n;i++)
			cin >> p[i];
		sort(p,p+n);
		bool flag = 0;
		long long sum=0;
		for(i=n-1;i>=0;i--){
			sum += p[i];
			if(sum>=m){
				flag = 1;
				break;
			}
		}
		if(!flag) cout <<"-1" << endl;
		else cout << n-i << endl;
		
	}
	return 0;
}

