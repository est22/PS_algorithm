#include <iostream>
using namespace std;

int main(){
    int amount;
    cin >> amount;

    int count = 0;
    int coins[] = {500,100,50,10};

    for (int i = 0; i < 4; i++){
        int coin = coins[i];
        count += amount /  coin ;
        amount %= coin;

    }
    cout << count << '\n';

}