#include <iostream>
using namespace std;

void Tabel(int jumlah){
	int a[100];
	int Balita=0,Anak=0,Remaja=0,Dewasa=0,Baya=0,Tua=0,LanjutUsia=0;
	int umur;
	
    for(int k=1; k<=jumlah; k++){
	   	cout<<"umur ke-"<<k<<":";
	   	cin>>umur;
   		a[k]=umur;
   	 if (umur>0 && umur<=5){
   		Balita+=1;	
   } if (umur>5 && umur<=13){
   		Anak+=1;
   } if (umur>13 && umur<17){
   		Remaja+=1;	
   } if (umur>17 && umur<=45){
   		Dewasa+=1;	
   } if (umur>45 && umur<=65){
   		Baya+=1;
   } if (umur>65 && umur<100){
   		Tua+=1;	
   } if (umur>=99){
   		LanjutUsia+=1;
   }
} 

   cout << "============================= \n";
   cout << "Kategori Usia : \n";
   cout << "Balita "	  <<Balita<<endl;
   cout << "anak-anak "  <<Anak<<endl;
   cout << "Remaja "	  <<Remaja<<endl;
   cout << "Dewasa "	  <<Dewasa<<endl;
   cout << "Paruh Baya " <<Baya<<endl;
   cout << "Orang tua "  <<Tua<<endl;
   cout << "Lansia "	  <<LanjutUsia<<endl;
   cout << "============================= \n";
   cout<<"isi inputan adalah : ";
   for(int k=1; k<=jumlah; k++){
	cout<<a[k]<<"-";
	}
}
