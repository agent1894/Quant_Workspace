#include <stdio.h>

int main(void)
{
    const char A = 'A';
    char center_char;
    int level;
    printf("Enter the character in center: ");
    scanf("%c", &center_char);
    level = center_char - A + 1;
    for (int i = 0; i < level; i++)
    {
        for (int x = 0; x < level - i - 1; x++)
        {
            printf(" ");
        }
        for (int x = 0; x < i; x++)
        {
            printf("%c", A + x);
        }
        printf("%c", A + i);
        for (int x = 1; x < i + 1; x++)
        {
            printf("%c", A + i - x);
        }
        for (int x = 0; x < level - i - 1; x++)
        {
            printf(" ");
        }

        printf("\n");
    }

    return 0;
}