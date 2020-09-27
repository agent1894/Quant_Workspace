#include <stdio.h>

int main(void)
{
    int first_operand;
    int second_operand;
    int mod;
    printf("This program computes moudli.\n");
    printf("Enter an integer to serve as the second operand: ");
    scanf("%d", &second_operand);
    printf("Now enter the first operand: ");
    scanf("%d", &first_operand);
    while (first_operand > 0)
    {
        mod = first_operand % second_operand;
        printf("%d %% %d is %d\n", first_operand, second_operand, mod);
        printf("Enter next number for first operand (<= 0 to quit): ");
        scanf("%d", &first_operand);
    }
    printf("Done\n");

    return 0;
}