#include <stdio.h>

void sort_variables(double *x, double *y, double *z);

int main(void)
{
    double x, y, z;
    printf("Enter three numbers, q to quit: ");
    while (scanf("%lf %lf %lf", &x, &y, &z) == 3)
    {
        printf("The original three numbers are x = %lf, y = %lf, z = %lf\n", x, y, z);
        sort_variables(&x, &y, &z);
        printf("After sorting variables, x = %lf, y = %lf, z = %lf\n", x, y, z);
        printf("Enter three numbers, q to quit: ");
    }
    printf("Bye.\n");

    return 0;
}

void sort_variables(double *x, double *y, double *z)
{
    double temp;
    if (*x > *y)
    {
        temp = *x;
        *x = *y;
        *y = temp;
    }
    if (*x > *z)
    {
        temp = *x;
        *x = *z;
        *z = temp;
    }
    if (*y > *z)
    {
        temp = *y;
        *y = *z;
        *z = temp;
    }
}