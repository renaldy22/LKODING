#include <iostream>
#include "header.h"

using namespace std;

int main(){
	int x, i, n, data[25];
	int banyaknya;
	banyaknya = masukkan();
	Input(data,banyaknya);
	cout << "ganjil: ";
	Ganjil(data,banyaknya);
	cout << "\ngenap: ";
	Genap(data,banyaknya);		
}
