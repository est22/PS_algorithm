#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_N   1000
typedef long long ll;

int A[MAX_N], B[MAX_N];
vector<int> subA, subB;

int main(){
    ll X, Y, R, Z;

    scanf("%lld %lld", &X, &Y);
    R = Y * 100 / X;

    if (R >= 99) printf("-1\n");
    else {
        ll low = 0, high = X, mid;
        while (low <= high) {
            mid = (low + high) >> 1; //2로 나눈 효과를 냄.
            if ( (Y + mid) * 100 / (X + mid) > R) high =  mid - 1;
            else low = mid + 1;
        }
        printf("&lld\n", high + 1);
    }

    return 0;

}