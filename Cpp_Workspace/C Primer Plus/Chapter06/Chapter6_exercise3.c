#include <stdio.h>

int main(void)
{
    char start;
    int ascii_char;
    int len;
    printf("Enter start character: ");
    scanf("%c", &start);
    ascii_char = (int)start;
    len = ascii_char - (int)('A');
    for (int i = 0; i < len + 1; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("%c", ascii_char - j);
        }
        printf("\n");
    }
    return 0;
}