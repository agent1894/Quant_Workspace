#include <stdio.h>

double power(double n, int p);

int main(void)
{
    double x, xpow;
    int exp;

    printf("Enter a number and the integer power");
    printf(" to which\n the number will be raised. Enter q");
    printf(" to quit.\n");
    while (scanf("%lf %d", &x, &exp) == 2)
    {
        xpow = power(x, exp);
        printf("%.3g to the power %d is %.5g\n", x, exp, xpow);
        printf("Enter next pair of numbers or q to quit.\n");
    }
    printf("Hope you enjoyed this power trip -- bye!\n");

    return 0;
}

double power(double n, int p)
{
    double pow = 1;
    int i;

    if (n != 0)
    {
        if (p > 0)
        {
            for (i = 1; i <= p; ++i)
            {
                pow *= n;
            }
        }
        else if (p < 0)
        {
            for (i = 1; i <= -p; ++i)
            {
                pow *= n;
            }
            pow = 1.0 / pow;
        }
        else
        {
            pow = 1;
        }
        
    }
    else
    {
        if (p == 0)
        {
            printf("0 to the power 0 is undefined, set to 1. ");
        }
        else
        {
            pow = 0;
        }
        
    }
    
    return pow;
}