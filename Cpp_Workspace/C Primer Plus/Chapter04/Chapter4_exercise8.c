#include <stdio.h>
const float GALLON_TO_LITER = 3.785;
const float MILE_TO_KM = 1.609;

int main(void)
{
    float miles;
    float gas;
    float mpg;
    float liter_to_km;
    printf("Enter miles: ");
    scanf("%f", &miles);
    printf("Enter gasoline in gallon: ");
    scanf("%f", &gas);
    mpg = miles / gas;
    printf("%.1f miles and %.1f gasoline consumption equals to %.1f MPG\n", miles, gas, mpg);
    liter_to_km = 1.0 / (mpg * MILE_TO_KM / 100 / GALLON_TO_LITER);
    printf("%.1f MPG equals to %.1f liters per 100km\n", mpg, liter_to_km);

    return 0;
}