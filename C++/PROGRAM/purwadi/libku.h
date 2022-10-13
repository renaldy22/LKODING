#ifndef librariku
#define librariku

#include <iostream>
using namespace std;
void tayangkan(int a[],int n) {
	int i;
	cout<<"\ndatanya ";
	for (i=1; i<=n; i++) {
		cout<<a[i]<<"  ";
	}
}

float cariR(int a[],int n)
{
   float jumlah=0;
	int i;
	for (i=1; i<=n; i++) {
		jumlah=jumlah+a[i];
	}
	return(jumlah*1.0/n);
}
void membesar(int a[], int n) { //procedure seleksi mengecil
	int i,j;
	int temp,x;
	for (i=1; i<=n-1; i=i+1) {
		x=i;
		for (j=i+1; j<=n; j++) {
			if (a[x]<a[j]) {
				x=j;
			}
		}
		///tukar
		temp=a[i];
		a[i]=a[x];
		a[x]=temp;
		tayangkan(a, n) ;
	}
}
int masukkan(void) { //fungsi
	int n;
	cout<<"\nBanyak element =?";
	cin>>n;
	return(n);
}

void inmatrik(int a[], int n) {
	int i;
	for (i=1; i<=n; i=i+1) {
		cout<<"\Elemen ke-"<<i<<" adalah ";
		cin>>a[i];
	}
}

float tengah(int a[],int n)
{
	if ((n%2)==0) { //genap
		return((a[n/2]+a[n/2+1])*1.0/2);
	} else { //ganjil
		return(a[n/2+1]);
	}
}
#endif
