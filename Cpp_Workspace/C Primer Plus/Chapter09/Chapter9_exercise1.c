#include <stdio.h>

double min(double x, double y);

int main(void)
{
    double x, y, min_of_x_y;
    printf("Enter two numbers, q to quit.\n");
    while (scanf("%lf %lf", &x, &y) == 2)
    {
        min_of_x_y = min(x, y);
        printf("The smaller one of %lf and %lf is %lf\n", x, y, min_of_x_y);
        printf("Enter two numbers, q to quit.\n");
    }
    printf("Bye.\n");

    return 0;
}

double min(double x, double y)
{
    return (x < y) ? x : y;
}