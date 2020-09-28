#include <stdio.h>

int main(void)
{
    const double INTEREST_RATE = 0.08;
    const double WITHDRAW = 10;
    int year = 0;
    double prize = 100;
    while (prize > 0)
    {
        prize *= (1 + INTEREST_RATE);
        prize -= WITHDRAW;
        year++;
    }
    printf("At year %d, all money withdrawed.\n", year);

    return 0;
}