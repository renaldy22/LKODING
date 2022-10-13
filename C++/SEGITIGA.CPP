
#include <iostream>




using namespace std;




int main() {
    int n = 5;
    cout << "==PROGRAM SEGITIGA CPP==" << endl;
    cout << "\n--segitiga siku-siku 1--" << endl << endl;
    //segitiga siku-siku 1
        for(int i = 0; i < n; i++){
            for(int j = 0; j <= i; j++) {
                cout << "*";
            } cout << endl;
        }




    cout << endl << endl;


    cout << "--segitiga siku-siku 2--" << endl << endl;


    //segitiga siku-siku 2


            for(int i = 0; i < n; i++){


            for(int j = n; j > i; j--) {


                cout << " ";


            } 


            for(int a = 0; a <= i; a++){


                cout << "*";


            } cout << endl;


        }




    cout << endl << endl;


    cout << "--segitiga piramida kelipatan ganjil--" << endl << endl;


    //segitiga siku-siku 3


    for(int i = 0; i < n; i++) {


        for(int j = n; j > i; j--) {


            cout << " ";


        } 


        for(int a = 0; a < (2*i - 1); a++) {


            cout << "*";


        } 


        cout << endl;


    }




    cout << "\n--segitiga siku-siku terbalik--" << endl << endl;


    //segitiga siku-siku 4


        for(int i = 0; i < n; i++){


            for(int j = n; j > i; j--) {


                cout << "*";


            } cout << endl;


        }




     cout << "\n--segitiga siku-siku terbalik 2--" << endl << endl;


    //segitiga siku-siku 5


        for(int i = 0; i < n; i++){


            for(int j = 0; j < i; j++) {


                cout << " ";


            } 


            for(int k = n; k > i; k--) {


                cout << "*";


            } cout << endl;


        }




    cout << endl << endl;


    cout << "--segitiga piramida kelipatan ganjil--" << endl << endl;


    //segitiga siku-siku 3


    for(int i = 0; i < n; i++) {


        for(int j = 0; j < i; j++) {


            cout << " ";


        } 


        for(int a = n; a >= (2*i - 1); a--) {


            cout << "*";


        } 


        cout << endl;


    }


    


    cin.get();


    return 0;


}
