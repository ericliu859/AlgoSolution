#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int main(){
	int t,n,i,j,k;
	long long m,p[8];
	cin >> t;
	while(t--){
		cin >> n >> m;
		for(i=0;i<n;i++)
			cin >> p[i];
		sort(p,p+n);
		int res = 0;
		bool flag=0;
		for(i=n-1;i>=0;i--){
			m -= p[i];
			res++;
			if(m==0) break;
			else if(m<0){
				res--;
				m+=p[i];
				for(j=0;j<n;j++){
					if(p[j]>m){
						for(k=j-1;k>=0;k--){
							if(m-p[k]>=0){
								m-=p[k];
								res++;
							}
							else{
								flag = 1;
								break;
							}
						}
						if(flag) break;
					}
				}
				if(flag) break;
			}
		}
		if(i==-1) cout << "-1" << endl;
		else cout << res << endl;
		
	}
	return 0;
}
