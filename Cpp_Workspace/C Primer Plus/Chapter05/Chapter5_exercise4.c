#include <stdio.h>
const float FEET_TO_CM = 30.48;
const float INCH_TO_CM = 2.54;

int main(void)
{
    float height;
    int feet;
    float inches;
    printf("Enter a height in centimeters: ");
    scanf("%f", &height);
    while (height > 0)
    {
        feet = height / FEET_TO_CM;
        inches = (height - feet * FEET_TO_CM) / INCH_TO_CM;
        printf("%.1f cm = %d feet, %.1f inches\n", height, feet, inches);
        printf("Enter a height in centimeters (<= 0 to quit): ");
        scanf("%f", &height);
    }
    printf("bye\n");

    return 0;
}