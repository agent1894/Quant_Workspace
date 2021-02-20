#include <stdio.h>
#include <ctype.h>

#define A_NUM (int) 'A'

int check_alpha(char ch);

int main(void)
{
    char ch;
    int num;

    while ((ch = getchar()) != EOF)
    {
        num = check_alpha(ch);
        if (num != -1)
        {
            printf("%c is character and it is number %d at alphabet.\n", ch, num);
        }
        else
        {
            printf("%c is not a character.\n", ch);
        }
    }

    printf("Bye.\n");

    return 0;
}

int check_alpha(char ch)
{
    if (isalpha(ch))
    {
        return (int) toupper(ch) - A_NUM;
    }
    else
    {
        return -1;
    }
}