#include <stdio.h>

int main(void)
{
    double sum_1 = 1.0;
    double sum_2 = 1.0;
    int count;
    double sign = 1.0;
    printf("Enter counts of series: ");
    scanf("%d", &count);
    for (double i = 2.0; i < (double)count + 1; i++)
    {
        sign *= -1;
        sum_1 += 1.0 / i;
        sum_2 += sign * (1.0 / i);
    }
    printf("Sum of Series 1 is: %lf\n", sum_1);
    printf("Sum of Series 2 is: %lf\n", sum_2);

    return 0;
}