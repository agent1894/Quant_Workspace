#include <stdio.h>
void show_arr(double const ar[], int num);
void reverse_arr(double *ar, int num);

int main(void)
{
    double ar_odd[5] = {2.55, -9.58, 1.21, 5.57, -6.31};
    double ar_even[6] = {-3.12, 2.54, 1.04, -5.74, 6.21, 1.1};
    int i;

    printf("The origin array is:\n");
    show_arr(ar_odd, 5);
    printf("The reverse array is:\n");
    reverse_arr(ar_odd, 5);
    show_arr(ar_odd, 5);

    printf("The origin array is:\n");
    show_arr(ar_even, 6);
    printf("The reverse array is:\n");
    reverse_arr(ar_even, 6);
    show_arr(ar_even, 6);

    return 0;
}

void reverse_arr(double *ar, int num)
{
    int mid = num / 2;
    int i;
    double temp;

    for (i = 0; i < mid; ++i)
    {
        temp = ar[i];
        ar[i] = ar[num - i -1];
        ar[num - i - 1] = temp;
    }
}

void show_arr(double const ar[], int num)
{
    int i;
    for (i = 0; i < num; ++i)
    {
        printf("%f ", ar[i]);
    }
    putchar('\n');
}