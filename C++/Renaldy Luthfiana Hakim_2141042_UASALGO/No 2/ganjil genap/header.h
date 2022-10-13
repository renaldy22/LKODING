#ifndef librariku
#define librariku
#include <iostream>

using namespace std;

int Ganjil(int data[],int n){
	int x,i;
	for (int i = 0; i <= n; i++){
		if (data[i] %2!=0){
			cout << data[i] <<" ";
			} 
	}
}

int Genap(int data[],int n){
	int x,j;
	for (int j=1; j<= n; j++){
		if (data[j] % 2 == 0){
		cout << data[j] << " ";
		}
	}
}

void Input(int data[], int n) {
	int i;
	for (i=1; i<=n; i=i+1) {
		cout<<"\Elemen ke-"<<i<<" adalah ";
		cin>>data[i];
	}
}

int masukkan(void) { //fungsi
	int n;
	cout<<"\nBanyak element =?";
	cin>>n;
	return(n);
}
#endif
