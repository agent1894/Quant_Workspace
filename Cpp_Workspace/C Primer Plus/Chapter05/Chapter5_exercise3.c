#include <stdio.h>
const int DAYS_A_WEEK = 7;

int main(void)
{
    int input_days;
    int week;
    int day;
    printf("Enter days to convert (positive integer, else quit): ");
    scanf("%d", &input_days);
    while (input_days > 0)
    {
        week = input_days / DAYS_A_WEEK;
        day = input_days % DAYS_A_WEEK;
        printf("%d days are %d weeks, %d days.\n", input_days, week, day);
        printf("Enter days to convert (positive integer, else quit): ");
        scanf("%d", &input_days);
    }
    
    return 0;
}