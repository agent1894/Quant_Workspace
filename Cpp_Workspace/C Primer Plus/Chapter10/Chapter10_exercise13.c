#include <stdio.h>
#define ROW 3
#define COL 5
int save_arr(double arr[][COL], int const row);
double single_arr_mean(double *arr);
double arr_mean(double const arr[][COL], int const row);
double arr_max(double const arr[][COL], int const row);
void show_arr(double const arr[][COL], int const row);

int main(void)
{
    int return_code;
    double arr[ROW][COL];
    double single_mean, mean, max;

    printf("Enter data:\n");
    return_code = save_arr(arr, ROW);
    if (return_code)
    {
        show_arr(arr, ROW);
        for (int i = 0; i < ROW; ++i)
        {
            single_mean = single_arr_mean(*(arr + i));
            printf("Group%2d mean: %.2f\n", i + 1, single_mean);
        }

        mean = arr_mean(arr, ROW);
        printf("Average of all data: %.2f\n", mean);

        max = arr_max(arr, ROW);
        printf("Maximum of all data: %.2f\n", max);
    }
    else
    {
        printf("Bye.\n");
    }

    return 0;
}

int save_arr(double arr[][COL], int const row)
{
    for (int i = 0; i < row; ++i)
    {
        printf("Enter 5 data in group%2d: ", i + 1);
        for (int j = 0; j < COL; ++j)
        {
            if (scanf("%lf", *(arr + i) + j) != 1)
            {
                return 0;
            }
        }
    }

    return 1;
}

double single_arr_mean(double *arr)
{
    double tot = 0;

    for (int i = 0; i < COL; ++i)
    {
        tot += *(arr + i);
    }

    return tot / COL;
}

double arr_mean(double const arr[][COL], int const row)
{
    double tot = 0;

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            tot += arr[i][j];
        }
    }

    return tot / (double) (COL * row);
}

double arr_max(double const arr[][COL], int const row)
{
    double max = **arr;

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            max = arr[i][j] > max ? arr[i][j] : max;
        }
    }

    return max;
}

void show_arr(double const arr[][COL], int const row)
{
    printf("The 2d array is:\n");
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < COL; ++j)
        {
            printf("%.2f ", arr[i][j]);
        }
        putchar('\n');
    }
}