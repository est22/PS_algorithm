#include <cstdio>

#define SZ_STK 1000

struct Stk {
    int arr[SZ_STK];
    int idx;

    void init(const int& n) {
        arr[idx = 0] = n;
    }

    bool num(const int& n){
        ++idx;
        arr[idx] = n;
        return true;
    }

    bool pop() {
        if (idx >= 0) {
            --idx;
            return true;
        }
        else{return false;}
    }
    bool inv(){
        if (idx < 0) return false;
        arr[idx] *= -1;
        return true;

    }

    bool swp(){
        if (idx < 1) return false;

        int t = arr[idx];
        arr[idx] = arr[idx-1];
        arr[idx -1] = t;
        return true;
    }

    bool add(){
        if (idx < 1) return false;
        arr[idx - 1] += arr[idx];
        --idx;
        return true;


    }

    bool sub(){

    }

    bool mul(){

    }

    bool div(){

    }

    bool mod(){

    } 
} gostk;

struct Order{
    int ordType;
    int n;

} orders[10000];

int main(){

    return 0;
}