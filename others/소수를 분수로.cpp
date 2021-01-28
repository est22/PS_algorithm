// 5376
// 614285.7142857142857142857 = 1000000 * a
// -    0.6142857142857142857 = a
// --------------------------------------------
// 614285.1   <- 뺀 결과        = 9999990 * a

// a = (6142857 - 6) / 9999990
// 이 부분에서 반복된 숫자 수 (6개)만큼 9가 나오고, 반복이 안된 길이(0.614~에서 6, 즉 1개)만큼 0이 나옴.

#include <cstdio>
#include <vector>

using namespace std;


int main(){
    char nums[30];
    int cnts[2] = {0, 0}; 
    int i;
    int t = 0; //type: 반복되지 않은 숫자 개수
    int cur = 0, pre = 0;

    scanf("%s", nums);
    i = 1;
    while (nums[++i] != '\0'){
        if (nums[i] == '(' ) t = 1, pre = cur;
        else if (nums[i] != ')') {
                cnts[t]++;
                cur = cur * 10 + nums[i] - '0';
        }
        
    }
    int d = cur - pre;
    int m = 0;

    for (i = 0; i < cnts[1]; ++i) m = m * 10 + 9;
    if ( m == 0) m = 1;
    for (i = 0; i < cnts[0]; ++i) m *= 10;
    
    return 0;
}