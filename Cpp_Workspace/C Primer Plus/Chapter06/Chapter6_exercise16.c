#include <stdio.h>

int main(void)
{
    const double PRINCIPAL = 100;
    const double SIMPLE_INTEREST_RATE = 0.1;
    const double COMPOUNDED_INTEREST_RATE = 0.05;
    double daphne = PRINCIPAL;
    double deirdre = PRINCIPAL;
    int year = 0;
    while (deirdre <= daphne)
    {
        year++;
        daphne += PRINCIPAL * SIMPLE_INTEREST_RATE;
        deirdre *= (1 + COMPOUNDED_INTEREST_RATE);
    }
    printf("At year %d, Daphne has %.2lf, Deirdre has %.2lf\n", year, daphne, deirdre);

    return 0;
}