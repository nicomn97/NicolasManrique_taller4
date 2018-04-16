#include <iostream>
#include <fstream>
#include <math.h>
#include <ctime>
#include <complex>



using namespace std;
typedef complex<double> dcmplx;

int main (nt argc, char *argv[]) {
    const double PI = 3.14159265359;
    ifstream infile;
    infile.open(argv[1]);
    double ti, xi;
    double tmin=ti;
    double xmin;
    double tmax;
    double xmax;
    int k = 0;
    while (infile >> ti >> xi){
        if(k==0){
            tmin=ti;
            xmin=xi;
            tmax=ti;
            xmax=xi;
        }
        k++;
    }

    double t[k];
    double x[k];
    double tj, xj;
    int ind2 = 0;

    while (infile >> tj >> xj){
        t[ind2]=tj;
        x[ind2]=xj;
        if(tj>tmax){
            tmax=tj;
            xmax=xj;
        }
        else if(tj<tmin){
            tmin=tj;
            xmin=xj;
        }
    }

    infile.close();

    int n = 1000;
    double st = n;
    double tf[n];
    double xf[n];
    for(int ii=0; ii<n;ii++){
        tf[ii]=((tmax-tmin)*ii/st)+tmin;
    }

    
    for(int g=0; g<n;g++){
        double prov = 0;
        for( int j = 0; j < k; j++ ) {
        
            double lj=1.0;
            for( int i = 0; i < k; i++ ) {
                if(i!=j){
                    lj=lj*((tf[g]-t[i])/(t[j]-t[i]));
                }
            }
            prov += lj*x[j];
        }
    xf[g]=prov;
    }


// tf y xf son los pares de tiempo espaciados. Dimension : n pares

    dcmplx dft[n];
    dcmplx img(0,1);
    dcmplx ze;
    ze = exp(-2*PI*img/n);
    
    for(int g1=0; g1<n;g1++){
        
        for(int g2=1; g2<n;g2++){
            dft[g1]+=(xf[g2]*(ze**(g1*g2)));
        }
    }
    
   double omega[n];
    for(int ifi1=0; ifi1<n;ifi1++){        
        omega[ifin]=(2*PI*ifi1)/(tmax-tmin);
    }   
   ofstream outfile;
   outfile.open("transformada.txt");
    for(int ifi=0; ifi<n;ifi++){        
        outfile << omega[ifi] <<" "<< dft[ifi].real <<" "<< dft[ifi].imag  << endl;
    }
   


   outfile.close();


    return 0;
}




