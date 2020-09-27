#include <stdio.h>

int main(void)
{
    int count, sum, end;
    count = 0;
    sum = 0;
    printf("Enter the end of days: ");
    scanf("%d", &end);
    while (count < end)
    {
        count++;
        sum = sum + count;
    }
    printf("sum = %d\n", sum);

    return 0;
}