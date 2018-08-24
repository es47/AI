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

int HC(int *board, int flag)        // use hill climbing
{
    int i, j, k, board_copy[RANGE], moves[RANGE][RANGE], now_cost, len;
    flag = 1;
    for (i = 0; i < RANGE; i++)
        for (j = 0; j < RANGE; j++)
            moves[i][j] = 100000;
    for (i = 0; i < RANGE; i++)             // move each queen to the different row
        for (j = 0; j < RANGE; j++)
        {
            if (board[i] == j)
                continue;
            for (k = 0; k < RANGE; k++)
                board_copy[k] = board[k];
            board_copy[i] = j;
            moves[i][j] = heuristic(board_copy);        // compute each move's attack number
        }
    now_cost = heuristic(board);        //compute present attack number
    for (i = 0; i < RANGE; i++)             // find if there exists a lower attack number
        for(j = 0; j < RANGE; j++)
            if (moves[i][j] < now_cost)
            {
                now_cost = moves[i][j];
                flag = 0;
            }
    len = 1;
    for (i = 0; i < RANGE; i++)             // find the number same as the lowest attack number
        for (j = 0; j < RANGE; j++)
        {
            if (moves[i][j] == now_cost)
            {
                moves[i][j] = len;
                len++;
            }
            else
                moves[i][j] = 10000;
        }
    if (len != 1)           // if there exists over one number
    {
        srand(time(NULL));
        k = rand() % (len - 1) + 1;         // random choose one
        for (i = 0; i < RANGE; i++)
            for (j = 0; j < RANGE; j++)
                if (moves[i][j] == k)
                    board[i] = j;
    }
    return flag;
}

int main()
{
    int board[RANGE], i, flag, count;
    clock_t start, end;
    srand(time(NULL));
    for (i = 0; i < RANGE; i++)         // set start board
        board[i] = rand() % RANGE;
    count = flag = 0;
    cout << "start board : ";
    start = clock();
    while(flag == 0)
    {
        for (i = 0; i < RANGE - 1; i++)
            cout << board[i] << ", ";
        cout << board[RANGE - 1] << endl;
        flag = HC(board, flag);
        count++;
    }
    end = clock();
    cout << endl << "attack = " << heuristic(board) << endl;
    cout << "step = " << count - 1 << endl;
    cout << "time = " << (end - start) << "ms" << endl;
    return 0;
}
