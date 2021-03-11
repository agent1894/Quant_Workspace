#include <stdio.h>
#define COL 3
#define ROW 5
void copy_arr(double target[], double const source[], int const num);
void show_arr2d(double const (*ar)[COL], int const row);

int main(void)
{
    double source2d[ROW][COL] = {{2.1, 6.5, -3.2}, {6.6, -1.2, -3.1}, {1.6, 4.5, 8.7}, {1.4, 7.6, -2.1}, {8.4, -2.2, 0.3}};
    double target2d[ROW][COL];
    int i;

    printf("Source 2d array is:\n");
    show_arr2d(source2d, ROW);
    printf("Copy to target 2d array\n");
    for (i = 0; i < ROW; ++i)
    {
        copy_arr(target2d[i], source2d[i], COL);
    }
    show_arr2d(target2d, ROW);

    return 0;
}

void show_arr2d(double const (*ar)[COL], int const row)
{
    int i, j;

    for (i = 0; i < row; ++i)
    {
        for (j = 0; j < COL; ++j)
        {
            printf("%.2f ", ar[i][j]);
        }
        putchar('\n');
    }
}

void copy_arr(double target[], double const source[], int const num)
{
    int i;
    
    for (i = 0; i < num; ++i)
    {
        target[i] = source[i];
    }
}