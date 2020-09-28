#include <stdio.h>

int main(void)
{
    int friends = 5;
    int week = 0;
    while (friends <= 150)
    {
        week++;
        friends -= week;
        friends *= 2;
    }
    printf("At week %d, Dr.Rabnud has %d friends.\n", week, friends);

    return 0;
}