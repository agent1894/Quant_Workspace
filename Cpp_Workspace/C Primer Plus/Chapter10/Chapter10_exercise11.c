#include <stdio.h>
#define COL 5
void show_arr(int const arr[][COL], int const row);
void double_arr(int arr[][COL], int const row);

int main(void)
{
    int array2d[3][COL] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {-5, -4, -3, -2, -1}};

    printf("Show origin array:\n");
    show_arr(array2d, 3);
    printf("Show doubled array:\n");
    double_arr(array2d, 3);
    show_arr(array2d, 3);

    return 0;
}

void show_arr(int const arr[][COL], int const row)
{
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            printf("%d ", arr[i][j]);
        }
        putchar('\n');
    }
}

void double_arr(int arr[][COL], int const row)
{
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            arr[i][j] *= 2;
        }
    }
}