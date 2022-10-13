#include <iostream>
using namespace std;


void Caribil(int isi[],int n){
	int i, j, nilai, b=0, cari=0;
	cout<<"\n== Isi Array =="<<endl;
    for(i=0; i<n; i++)
    {
        cout<<"Isi indek ke ["<<i<<"]"<<" = ";
        cin>>isi[i];
    }
    cout<<"\nMasukan Nilai Yang Ingin dicari = ";
    cin>>nilai;
    for(i=0; i<n; i++)
    {
        if(nilai==isi[i])
        {
             cari=nilai;
             b=i;
        }
    }
    if(nilai==cari)
    {
        cout<<"\n Nilai Yang dicari ("<<nilai<<") "<<"ditemukan di Indek ke ["<<b<<"] \n";
    }else{
        cout<<"\n Nilai Yang dicari ("<<nilai<<") "<<"Tidak ditemukan \n";
    }
}

int masukan(void){
	int n;
	cout<<"Masukan Jumlah Array = ";
    cin>>n;
    return(n);
}
