#include <stdio.h>

int main(void)
{
    float inch_to_cm = 2.54;
    float height;
    printf("Enter the height in inches: ");
    scanf("%f", &height);
    printf("The height of %f inches is %f cm\n", height, height * inch_to_cm);

    return 0;
}