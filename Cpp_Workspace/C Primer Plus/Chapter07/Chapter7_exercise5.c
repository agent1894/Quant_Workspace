#include <stdio.h>

int main(void)
{
    char ch;
    unsigned int cnt = 0;
    printf("Enter a sentence with # to stop.\n");
    while((ch = getchar()) != '#')
    {
        switch (ch)
        {
        case '.':
        {
            printf("!");
            cnt++;
            break;
        }

        case '!':
        {
            printf("!!");
            cnt++;
            break;
        }
        
        default:
            printf("%c", ch);
            break;
        }
    }
    printf("\nReplace %d times.\n", cnt);

    return 0;
}