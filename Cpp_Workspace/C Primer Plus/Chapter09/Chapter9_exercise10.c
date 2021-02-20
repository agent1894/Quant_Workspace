#include <stdio.h>

void to_base_n(unsigned long n, unsigned int m);

int main(void)
{
    unsigned long number;
    unsigned int system, count;
    printf("Enter an integer (q to quit):\n");
    while (scanf("%lu", &number) == 1)
    {
        printf("Enter the system of numeration (q to quit):\n");
        while (count = scanf("%d", &system) == 1)
        {
            if (system < 2 || system > 10)
            {
                printf("system of numeration shouble be between 2-10. ");
            }
            else
            {
                break;
            }
        }
        if (count != 1)
        {
            break;
        }
        printf("Number equivalent: ");
        to_base_n(number, system);
        putchar('\n');
        printf("Enter an integer (q to quit):\n");
    }
    printf("Done.\n");

    return 0;
}

void to_base_n(unsigned long n, unsigned int m)
{
    int r;

    r = n % m;
    if (n >= m)
    {
        to_base_n(n / m, m);
    }
    putchar(r + '0'); // putchar use ASCII
}