#include <stdio.h>
void copy_vla(int const row, int const col, double target[row][col], double const source[row][col]);
void show_arr(int const row, int const col, double const ar[row][col]);

int main(void)
{
    int row = 3;
    int col = 5;
    double source[3][5] = {{1.5, 8.2, 1.7, 5.4, 2.0}, {4.4, 5.1, 2.7, 6.9, 4.1}, {0.8, 8.4, 1.5, 6.2, 7.7}};
    double target[row][col];

    printf("Show source array:\n");
    show_arr(row, col, source);
    printf("Copy array to VLA, show target array:\n");
    copy_vla(row, col, target, source);
    show_arr(row, col, target);

    return 0;
}

void copy_vla(int const row, int const col, double target[row][col], double const source[row][col])
{
    int i, j;

    for (i = 0; i < row; ++i)
    {
        for (j = 0; j < col; ++j)
        {
            target[i][j] = source[i][j];
        }
    }
}

void show_arr(int const row, int const col, double const ar[row][col])
{
    int i, j;

    for (i = 0; i < row; ++i)
    {
        for (j = 0; j < col; ++j)
        {
            printf("%.2f ", ar[i][j]);
        }
        putchar('\n');
    }
}