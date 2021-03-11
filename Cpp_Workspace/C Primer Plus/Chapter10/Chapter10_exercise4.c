#include <stdio.h>
#define LEN 5
int max_double_idx(double ar[], int num);

int main(void)
{
    double ar[LEN] = {4.2, -6.3, 1.8, 8.2, -19.5};
    int max_idx;

    max_idx = max_double_idx(ar, LEN);
    printf("Index for max double is: %d\n", max_idx);

    return 0;
}

int max_double_idx(double ar[], int num)
{
    double max = ar[0];
    int idx = 0;
    int i;

    for (i = 0; i < num; ++i)
    {
        if (ar[i] > max)
        {
            idx = i;
            max = ar[i];
        }
    }

    return idx;
}