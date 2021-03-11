#include <stdio.h>
void sum_arr(int const *ar1, int const *ar2, int *sum, int const num);
void show_arr(int const *ar, int const num);

int main(void)
{
    int ar1[4] = {2, 4, 5, 8};
    int ar2[4] = {1, 0, 4, 6};
    int num = 4;
    int sum[num];

    sum_arr(ar1, ar2, sum, num);
    printf("Show sum of two arraies.\n");
    show_arr(sum, num);

    return 0;
}

void sum_arr(int const *ar1, int const *ar2, int *sum, int const num)
{
    for (int i = 0; i < num; ++i)
    {
        *(sum + i) = *(ar1 + i) + *(ar2 + i);
    }
}

void show_arr(int const *ar, int const num)
{
    for (int i = 0; i < num; ++i)
    {
        printf("%d ", *(ar + i));
    }
    putchar('\n');
}