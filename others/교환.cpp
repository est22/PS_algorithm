#define NAX_N 50
#define MAX_L 7
//하다 말음.

int multi[MAX_L],nums[MAX_L];
bool visited[ MAX_N +1 ][1000001];


int backtracking(int n, int k){
    int i = 0;
    for (int j = 1; j < L; ++j){
        if (nums[j] != 0) {
            int buf = nums[i];
            nums[i] = nums[j], nums[j] = buf;
            backtracking(n +(mums[i]-nums[j])) * multi[i] + (nums[j]-nums[i])*multi[i]
            buf = nums[i];
            nums[i = nums[j], nums[j] = buf;
        }
        }
    }
}