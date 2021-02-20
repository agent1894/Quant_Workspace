#include <stdio.h>

void chline(char, int, int);

int main(void)
{
    char ch;
    int i, j;
    printf("Enter a character (new line to quit): ");
    while ((ch = getchar()) != '\n')
    {
        printf("Enter two integers to implement lines and columns: ");
        if (scanf("%d %d", &i, &j) != 2)
        {
            break;
        }
        chline(ch, i, j);
        getchar();
        printf("Enter a character (new line to quit): ");
    }

    printf("Bye.\n");

    return 0;
}

void chline(char ch, int i, int j)
{
    for (int m = 0; m < i; ++m)
    {
        for (int n = 0; n < j; ++n)
        {
            putchar(ch);
        }
        printf("\n");
    }
}