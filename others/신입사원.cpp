#include  <iostream>
#include  <algorithm>
using namespace std;

const int MAX = 100000;
int N;
pair<int,int> applicant[MAX];
int main()
{
int T;
cin >> T;
while (T--)
{
int cnt = 0;
cin >> N;
    for (int i = 0; i < N; ++i)
    {
    cin >> applicant[i].first >> applicant[i].second;
    }
    sort(applicant, applicant + N);
    cnt++; // 1등을 뽑는다.
    int bestscore = applicant[0].second;
    for (int i = 1; i < N; ++i) // 현재 뽑힌사람보다 서류순위는 낮지만(정렬됨) 면접순위가 높은 사람을 찾는다.
    {
        if (applicant[i].second < bestscore)
        {
        cnt++;
        bestscore = applicant[i].second; // 뽑힌사람의 면접순위로 갱신한다.
        }
    }   
cout << cnt << endl;
}
return 0;
}