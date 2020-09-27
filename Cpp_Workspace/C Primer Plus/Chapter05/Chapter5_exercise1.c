#include <stdio.h>
const int MINUTES = 60;

int main(void)
{
    int input_minutes;
    int minutes;
    int hours;
    printf("Enter minutes to convert (positive integer, else quit): ");
    scanf("%d", &input_minutes);
    while (input_minutes > 0)
    {
        hours = input_minutes / MINUTES;
        minutes = input_minutes % MINUTES; 
        printf("%d minutes equals to %d hours, %d minutes\n", input_minutes, hours, minutes);
        printf("Enter minutes to convert (positive integer, else quit): ");
        scanf("%d", &input_minutes);
    }

    return 0;
}