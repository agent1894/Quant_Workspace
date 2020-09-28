#include <stdio.h>

int main(void)
{
    int upper, lower;
    int num;
    int sum;
    printf("Enter lower and upper integer limits: ");
    num = scanf("%d %d", &lower, &upper);
    while (lower < upper)
    {
        sum = 0;
        for (int i = lower; i < upper + 1; i++)
        {
            sum += i * i;
        }
        printf("The sums of the squares from %d to %d is %d\n", lower * lower, upper * upper, sum);
        printf("Enter next set of limits: ");
        num = scanf("%d %d", &lower, &upper);
    }
    printf("Done\n");

    return 0;
}