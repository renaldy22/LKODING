#include <iostream>

using namespace std;

#include <stdio.h>
#include <iostream>
#include <conio.h>
using namespace std;
int A[10] = {12,24,13,25,10,11,21,20,15,18}; //variabel array beserta isi elemen
int bil, c;

void cari (int bil)  //fungsi mencari no indeks
{
 for (c = 0; c < 10; c++)
 { //menampilkan hasil no index yang dicari
  if (A[c] == bil)  //pemilihan jika masukan sama dengan isi elemen
  {
   cout << "Bilangan yang anda cari berada di indeks ke - " << c;
   break;
  }
 }
 getch ();
}

int main()
{
	 //menampilkan isi elemen array
	 for (int i = 0; i < 10; i++)
	 {
	  cout << "Indeks - [" << i << "]" << " " << A[i] << endl;
	 }
	 cout << endl;
	 
	 cout << "Masukan bilangan yang akan dicari : ";
	 cin >> bil;  //masukan bilangan
	 
	 cari (bil);  //pemanggilan paramameter
	
	 for (c = 0; c < 10; c++)
	 { //menampilkan jika tidak terdapat di dalam array
	  if (A[c] != bil)
	  {
	   cout << "Bilangan yang dicari tidak terdaftar";
	   break;
	  }
	}
	 return 0;
}

