#include <iostream>
#include <fstream>
#include <math.h>
#include <ctime>

using namespace std;


int main () {
    ifstream infile;
    infile.open("archivo.txt");
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

    return 0;
}




