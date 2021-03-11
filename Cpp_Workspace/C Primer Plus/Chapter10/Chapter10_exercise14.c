#include <stdio.h>
int save_arr(int const row, int const col, double arr[row][col]);
double arr_mean(int const row, int const col, double const arr[row][col]);
double arr_max(int const row, int const col, double const arr[row][col]);
void show_arr(int const row, int const col, double const arr[row][col]);

int main(void)
{
    int const col = 5;
    int const row = 3;
    double receive_data[row][col];
    int return_code;
    double mean, max;

    printf("Enter data:\n");
    return_code = save_arr(row, col, receive_data);
    if (return_code)
    {
        show_arr(row, col, receive_data);

        mean = arr_mean(row, col, receive_data);
        printf("Average of all data: %.2f\n", mean);

        max = arr_max(row, col, receive_data);
        printf("Maximum of all data: %.2f\n", max);
    }
    else
    {
        printf("Bye.\n");
    }
    
    return 0;
}

int save_arr(int const row, int const col, double arr[row][col])
{
    for (int i = 0; i < row; ++i)
    {
        printf("Enter %d data in Group%2d: ", col, i + 1);
        for (int j = 0; j < col; ++j)
        {
            if (scanf("%lf", *(arr + i) + j) != 1)
            {
                return 0;
            }        
        }
    }

    return 1;
}

double arr_mean(int const row, int const col, double const arr[row][col])
{
    double total = 0;

    for (int i = 0; i < row; ++i)
    {
        double subtotal = 0;
        for (int j = 0; j < col; ++j)
        {
            subtotal += arr[i][j];
        }
        printf("Group%2d mean: %.2f\n", i + 1, subtotal / (double) col);
        total += subtotal;
    }

    return total / (double) (row * col);
}

double arr_max(int const row, int const col, double const arr[row][col])
{
    double max = **arr;

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            max = arr[i][j] > max ? arr[i][j] : max;
        }
    }

    return max;
}

void show_arr(int const row, int const col, double const arr[row][col])
{
    printf("The 2d array is:\n");
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            printf("%.2f ", arr[i][j]);
        }
        putchar('\n');
    }
}