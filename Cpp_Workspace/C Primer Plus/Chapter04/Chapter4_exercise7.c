#include <stdio.h>
#include <float.h>

int main(void)
{
    double var_d = 1.0 / 3.0;
    double var_f = 1.0 / 3.0;
    printf("variable with double type: %.6f, variable with float type: %.6f\n", var_d, var_f);
    printf("variable with double type: %.12f, variable with float type: %.12f\n", var_d, var_f);
    printf("variable with double type: %.16f, variable with float type: %.16f\n", var_d, var_f);
    printf("float precision = %d digits\n", FLT_DIG);
    printf("double precision = %d digits\n", DBL_DIG);
}