#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

void menu(void);
float input_number(void);

int main(void)
{
    float input1, input2;
    char ch;
    int scan1, scan2;
    menu();

    while ((ch = getchar()) != 'q')
    {
        printf("Enter first number: ");
        input1 = input_number();
        printf("Enter second number: ");
        input2 = input_number();
        switch (ch)
        {
        case 'a':
            printf("%.2f + %.2f = %.2f\n", input1, input2, input1 + input2);
            break;
        case 's':
            printf("%.2f - %.2f = %.2f\n", input1, input2, input1 - input2);
            break;
        case 'm':
            printf("%.2f * %.2f = %.2f\n", input1, input2, input1 * input2);
            break;
        case 'd':
            while (input2 == 0)
            {
                printf("Enter a number other than 0: ");
                input2 = input_number();
            }
            printf("%.2f / %.2f = %.2f\n", input1, input2, input1 / input2);
            break;
        default:
            printf("Unsupported choice, please enter a, s, m ,d or q.\n");
            break;
        }
        menu();
        while (getchar() != '\n')
        {
            continue;
        }
    }
    printf("Bye.\n");

    return 0;
}

void menu(void)
{
    printf("Enter the operation of your choice:\n");
    printf("a. add          s. subtract\n");
    printf("m. multiply     d. divide\n");
    printf("q. quit\n");
}

float input_number(void)
{
    char ch;
    float num;
    while (scanf("%f", &num) != 1)
    {
        while ((ch = getchar()) != '\n')
        {
            putchar(ch);
        }
        printf(" is not an number.\n");
        printf("Please enter a number, such as 2.5, -1.78E8, or 3: ");
    }
    return num;
}