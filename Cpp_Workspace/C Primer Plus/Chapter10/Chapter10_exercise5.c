#include <stdio.h>
#define LEN 5
double diff_max_min(double ar[], int num);

int main(void)
{
    double ar[LEN] = {3.5, 4.9, -6.4, 5.1, -2.7};
    double diff;

    diff = diff_max_min(ar, LEN);
    printf("Diffenerce of max and min in array is: %f\n", diff);

    return 0;
}

double diff_max_min(double ar[], int num)
{
    double max, min;
    int i;

    max = min = ar[0];
    for (i = 0; i < num; ++i)
    {
        max = ar[i] > max ? ar[i] : max;
        min = ar[i] < min ? ar[i] : min;
    }

    return max - min;
}