#include <cstdio>

int DMax[3][MAX_N], DMin[3][MAX_N];

int dpMax(int loc, int n){
    // 기저조건
    if (n < 0) return 0;
    // Memoization
    if (DMax[loc][n] > 0) return DMMax[loc][n];    
    // 점화식
    DMax[loc][n] = Dmax[loc][n-1]; // 위에서 내려오는 경우
    if (loc > 0 && DMax[loc - 1][n - 1] > DMax[loc][n]{
        Dmax[loc][n] = DMax[loc - 1][n - 1];
    }
    if (loc < 2 && DMax[loc + 1][n -1] > DMax[loc][n]){
        DMax[loc][n] = Dmax[loc + 1][n -1];

    }
    DMax[loc][n] += nos[loc][n];
    return DMax[loc][n];

}

int main(){

    return 0;
}