#include <cstdio>

int gcd(int a, int b){
    int q, r, t;

    while (b != 0){
        r = a % b;
        a = b;
        b = r;
    }
    return 0;


}

int gcd2(int a, int b){
    if (b ==0) return ;
    else return gcd(b, a % b);
}

int main(){
    int a,b,c,g;

    g = gcd(a,b);
    g = gcd(g,c);

    return 0;
}