/*
 matrix_Gaussian_elimination.cpp
 Mencari invers dengan eliminasi Gauss
 20150201 | Sparisoma Viridi
*/
#include <cmath>
#include <iostream>

using namespace std;

void display(double x[], int N) {
    int M = N + 1;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            int k = M * i + j;
            cout << x[k];
            if(j < M - 1) cout << "\t";
        }
        cout << endl;
    }
}

int main(int argc, char *argv[]) {
    // Jumlah baris
    int N = 4;
    // Array 2 dimensi dalam array 1 dimensi
    double r[] = {
        1, 1, 1, 1, 10,
        4, 1, 3, 1, 19, 
        2, 1, 1, 1, 11,
        1, 3, 1, 2, 18,
    };
    /*
    double r[] = {
        1, 3, 4, 1, 12,
        0, 12, 0, 2, 4,
        0, 0, 2, 1, 1,
        0, 0, 0, 1, -1,
    };
    */

    // Tampilkan matriks awal
    cout << "Matriks awal" << endl;
    display(r, N);

    // Indeks array dimulai dari 0
    for(int k = 0; k < N - 1; k++) {
        for(int i = 1 + k; i < N; i++) {
            int ik = (N + 1) * i + k;
            double cik = r[ik];
            for(int j = k; j < N + 1; j++) {
                int ij = (N + 1) * i + j;
                int kj = (N + 1) * k + j;
                int kk = (N + 1) * k + k;
                r[ij] = r[ij] - cik * r[kj] / r[kk];
            }
        }
    }

    // Tampilkan matriks akhir
    cout << endl;
    cout << "Matriks berbentuk baris echelon" << endl;
    display(r, N);

    double x[N];
    for(int i = N-1; i >= 0; i--) {
        double c = 0;
        for(int j = N-1; j > i; j--) {
            int ij = (N + 1) * i + j;
            c = c + x[j] * r[ij];
        }
        int iM = (N + 1) * i + N;
        int ii = (N + 1) * i + i;
        x[i] = (r[iM] - c) / r[ii];
    }

    cout << endl;
    cout << "Solusi" << endl;
    
    for(int i = 0; i < N; i++) {
        cout << x[i] << endl;
    }

    return 0;
} 