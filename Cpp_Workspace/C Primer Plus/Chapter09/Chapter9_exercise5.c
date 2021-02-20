#include <stdio.h>

void larger_of(double *x, double *y);

int main(void)
{
    double x;
    double y;
    printf("Enter two numbers, q to quit: ");
    while (scanf("%lf %lf", &x, &y) == 2)
    {
        printf("Now two numbers are x = %lf and y = %lf\n", x, y);
        larger_of(&x, &y);
        printf("After filling larger of two numbers, x = %lf and y = %lf\n", x, y);
        printf("Enter two numbers, q to quit: ");
    }
    printf("Bye.\n");

    return 0;
}

void larger_of(double *x, double *y)
{
    *x = *y = *x < *y ? *y : *x;
}