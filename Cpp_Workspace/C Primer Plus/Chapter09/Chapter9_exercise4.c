#include <stdio.h>

double harmonic_mean(double x, double y);

int main(void)
{
    double x, y, mean;
    printf("Enter two numbers for calculating their harmonic_mean, q to quit: \n");
    while (scanf("%lf %lf", &x, &y) == 2)
    {
        mean = harmonic_mean(x, y);
        printf("The harmonic mean of %.4lf and %.4lf is %.4lf\n", x, y, mean);
        printf("Enter two numbers for calculating their harmonic_mean, q to quit: \n");
    }
    printf("Bye.\n");

    return 0;
}

double harmonic_mean(double x, double y)
{
    return 1.0 / ((1.0 / x + 1.0 / y) / 2.0);
}