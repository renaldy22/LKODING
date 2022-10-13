#include <iostream>
#include "libku.h"
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
//program utama
// dibuat oleh Purwadi tgl .....

int main(int argc, char** argv) {
	//masukkan matriksnya
	int M[20];
	int banyaknya;
	banyaknya=masukkan();
	inmatrik(M,banyaknya);
	//ditampilkan sebelum diurutkan
	cout<<"\nAslinyan :";
	tayangkan(M,banyaknya);
	//diurutkan
	membesar(M,banyaknya);
	//setelah diurutkan
	cout<<"\nDiurutkan :";
	tayangkan(M,banyaknya);
	//terbesar dan terkecil nya
	cout<<"\nTerkecil :"<<M[banyaknya];
	cout<<"\nTerbesar :"<<M[1];
	//bilangan di tengah
	cout<<"\nPosisi di tengah yaitu "<<tengah(M,banyaknya);
	//rerata
	cout<<"\nRata-ratanya :"<<cariR(M,banyaknya);
	
	return 0;
}
