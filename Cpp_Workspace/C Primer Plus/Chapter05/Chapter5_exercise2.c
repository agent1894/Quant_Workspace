#include <stdio.h>

int main(void)
{
    int input;
    int limit;
    printf("Enter an integer: ");
    scanf("%d", &input);
    limit = input + 10;
    while (input <= limit)
    {
        printf("%d ", input);
        input++;
    }

    return 0;
}