#include <stdio.h>
double cube(double n);

int main(void)
{
    double var;
    printf("Enter a double variable: ");
    scanf("%lf", &var);
    printf("The cube of input variable %lf is %lf\n", var, cube(var));
    
    return 0;
}

double cube(double n)
{
    return n * n * n;
}