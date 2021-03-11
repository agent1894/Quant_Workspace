#include <stdio.h>
#define LEN 5
int max_int(int const ar[], int num);

int main(void)
{
    int ar[LEN] = {3, 6, 8, 2, 1};
    int max = max_int(ar, LEN);

    printf("Max int in array is: %d\n", max);

    return 0;
}

int max_int(int const ar[], int num)
{
    int i;
    int max = ar[0];

    for (i = 0; i < num; ++i)
    {
        max = ar[i] > max ? ar[i] : max;
    }

    return max;
}