#include<iostream>
using namespace std;
int main(){
    int N,i,j;
    cout<<"Enter the value of N"<<endl;
    cin>>N;
    i=1;
    int val=1;
    while(i<=N){
        j=1;
        while(j<=i){
            cout<<val;
            j=j+1;
            val=val+1;
        }cout<<endl;
        i=i+1;

    }
}