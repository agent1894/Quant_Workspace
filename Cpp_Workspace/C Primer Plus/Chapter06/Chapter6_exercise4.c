#include <stdio.h>

int main(void)
{
    char character = 'A';
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("%c", character + j);
        }
        character += i + 1;
        printf("\n");
    }

    return 0;
}