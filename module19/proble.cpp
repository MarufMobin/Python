#include<bits/stdc++.h>
using namespace std;

int getSOD( long long x ){
    int sumOfDigits = 0;
    while( x ){
        int lastDigit = x % 10;
        sumOfDigits += lastDigit;
        x % 10;
    }
    return sumOfDigits;
}

bool isValid( long long x , long long s ){
    int sodx = getSOD(x);
    bool valid = ( x - sodx ) >= s;
    return valid;
}


int main(){
    long long n , s;
    cin >> n >> s;

    long long ans = -1 , lo = 0, hi = n;

    while( hi >= lo ){
        long long mid = ( hi + lo ) / 2;
        if( isValid( mid , s )){
            ans = mid;
            hi = mid - 1;
        }else{
            lo = mid + 1;
        }
    }
    cout << ( ans == -1 ) ? 0 : n - ans + 1; 
    return 0;
}