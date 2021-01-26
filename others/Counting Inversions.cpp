#include <cstdio>

#define MAX_N   1000000

int nos[MAX_N], buf[MAX_N], cnts[MAX_N]; // cnts:해당 i번째 인덱스에서 몇번 추월하는지
int ans = 0;

void merge(int from,int mid, int to){ //2.
    int i1 = from, i2 = mid, i = from; // 인덱스를 세개 잡음

    while (i1 < mid && i2 < to){
        if (nos[i2] < nos[i]) {
            buf[i++] = nos[i2++];
            // buf[i] = nos[i2];
            // ++i;
            // ++i2;
            ans += mid = i1; // 이 문제를 위해서 추가됨
        }
        else {
            buf[i++] = nos[i1++];
        }
    }
    while (i1 < mid){
        buf[i] = nos[i1];
        ++i;
        ++i1;
    }
    while (i2 < to) {
        buf[i] = nos[i2];
        ++i;
        ++i2;
    }
    for (i = from; i < to; ++i) nos[i] = buf[i];
}

void mergeSort(int from, int to){ // 1.
    if (from >= to - 1 ) return; // 탈출조건 정의

    int mid = (from+to) /2; //분할

    mergeSort(from, mid); //왼쪽에 대한 merge sort 재귀호출
    mergeSort(mid,to); //오른쪽에 대한 merge sort 재귀호출
    merge(from,mid,to); //정렬된 것 두개를 가지고 merge
}
int main(){
    return 0;
}