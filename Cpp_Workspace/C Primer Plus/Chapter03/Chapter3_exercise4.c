#include <stdio.h>

int main(void)
{
    double input_double;
    printf("Enter a floating-point value: ");
    scanf("%lf", &input_double);
    printf("fixed-point notation: %f\n", input_double);
    printf("exponential notation: %e\n", input_double);
    printf("p notation %a\n", input_double);

    return 0;
}
