#include <iostream>
#include <cstdlib>
#include <ctime>

#define RANGE 8
#define POPULATION 4

using namespace std;

int heuristic(int *board)          // compute the number of attack
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

int initialize(int **board)         // set the start population
{
    int i, j;
    srand(time(NULL));
    for (i = 0; i < POPULATION; i++)
        for (j = 0; j < RANGE; j++)
            board[i][j] = rand() % RANGE;
}

int good_parent(int **board, int *fit_parent)   // choose the first and the second good parent
{
    int min1, min2, i, cost[POPULATION], temp;
    min1 = min2 = 10000;
    fit_parent[0] = 1000;
    for (i = 0; i < POPULATION; i++)
    {
        cost[i] = heuristic(board[i]);
        if (cost[i] < min2)
        {
            min2 = cost[i];
            fit_parent[1] = i;
        }
        if (min2 < min1)
        {
            temp = min1;
            min1 = min2;
            min2 = temp;
            temp = fit_parent[0];
            fit_parent[0] = fit_parent[1];
            fit_parent[1] = temp;
        }
    }
}

int random_choose(int **board, int *parent, int *fit_parent)    // from the two goodest parent random choose one
{
    int choose, i;

    choose = rand() % 2;
    for (i = 0; i < RANGE; i++)
        parent[i] = board[fit_parent[choose]][i];
}

int crossover(int *parent1, int *parent2, int *child)
{
    int cut, i;
    cut = rand() % RANGE;               // random choose cut position
    for (i = 0; i < RANGE; i++)
    {
        if (i < cut)
            child[i] = parent1[i];
        else
            child[i] = parent2[i];
    }
}

int mutate(int *child)
{
    int row, col;
    row = rand() % RANGE;
    col = rand() % RANGE;
    child[col] = row;           // move one col's queen to another row
}

int GA(int **board, int flag)
{
    int i, mutate_pro, j, k;
    int *parent1, *parent2, *child, *fit_parent;
    int **new_board;

    new_board = new int*[POPULATION];
    for(i = 0; i < POPULATION; i++)
        *(new_board + i) = new int[RANGE];
    parent1 = new int[RANGE];
    parent2 = new int[RANGE];
    child = new int[RANGE];
    fit_parent = new int[2];

    good_parent(board, fit_parent);         // choose the first and the second good parent

    for (i = 0; i < POPULATION; i++)
    {
        random_choose(board, parent1, fit_parent);      // from the two goodest parent random choose one
        random_choose(board, parent2, fit_parent);

        crossover(parent1, parent2, child);         // produce new child

        mutate_pro = rand() % 2;            // choose mutate or not
        if (mutate_pro == 1)
            mutate(child);

        if (heuristic(child) == 0)
            flag = 1;

        for (j = 0; j < RANGE; j++)
            new_board[i][j] = child[j];
    }

    for (i = 0; i < POPULATION; i++)        //  change the whole generation
        for (j = 0; j < RANGE; j++)
            board[i][j] = new_board[i][j];

    for(i = 0; i < POPULATION; i++)
        delete [] (*(new_board + i));
    delete [] new_board;
    delete [] parent1;
    delete [] parent2;
    delete [] child;
    delete [] fit_parent;

    return flag;
}

int main()
{
    int flag, count, i, j;
    int **board;
    clock_t start, end;

    board = new int*[POPULATION];
    for(i = 0; i < POPULATION; i++)
        *(board + i) = new int[RANGE];

    initialize(board);
    srand(time(NULL));

    cout << "start population : " << endl;
    for (i = 0; i < POPULATION; i++)
    {
        for (j = 0; j < RANGE; j++)
            cout << board[i][j] << ", ";
        cout << endl;
    }

    start = clock();
    count = flag = 0;
    while(flag == 0)
    {
        flag = GA(board, flag);
        count++;
    }

    end = clock();

    cout << "step = " << count - 1 << endl;
    cout << "time = " << (end - start) << "ms" << endl;

    for(i = 0; i < POPULATION; i++)
        delete [] (*(board + i));
    delete [] board;

    return 0;
}
