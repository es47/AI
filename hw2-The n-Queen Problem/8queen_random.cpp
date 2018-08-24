#include <iostream>
#include <cstdlib>
#include <ctime>

#define RANGE 8             // set the range of the cheeseboard

using namespace std;

int heuristic(int board[])          // compute the number of attack
{
    int cost, i, j, offset;
    cost = 0;
    for (i = 0; i < RANGE; i++)
        for (j = i + 1; j < RANGE; j++)
        {
            if (board[i] == board[j])       // if on the same row, attack + 1
                cost++;
            offset = j - i;
            if (board[i] == board[j] - offset || board[i] == board[j] + offset)     // if on the diagonal, attack + 1
                cost++;
        }
    return cost;
}

int main()
{
    int board[RANGE], i, flag, count, queen, check[RANGE];
    clock_t start, end;
    srand(time(NULL));
    count = flag = 0;
    start = clock();
    while(flag == 0)
    {
        for (i = 0; i < RANGE; i++)
            check[i] = 0;
        i = 0;
        while (i < RANGE)
        {
            queen = rand() % RANGE;
            if (check[queen] != 1)
            {
                board[i] = queen;
                check[queen] = 1;
                i++;
            }
        }
        for (i = 0; i < RANGE; i++)
            cout << board[i] << ", ";
        cout << endl;
        if (heuristic(board) == 0)
            flag = 1;
        count++;
    }
    end = clock();
    cout << endl << "attack = " << heuristic(board) << endl;
    cout << "step = " << count - 1 << endl;
    cout << "time = " << (end - start) << "ms" << endl;
    return 0;
}

