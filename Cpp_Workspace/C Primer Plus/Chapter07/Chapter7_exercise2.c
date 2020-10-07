#include <stdio.h>

int main(void)
{
    const unsigned int LINE = 8;
    unsigned int ch_cnt = 0;
    char ch;
    printf("Enter a sentence with # to stop.\n");
    while ((ch = getchar()) != '#')
    {
        if (ch_cnt % LINE == 0 && ch_cnt != 0)
        {
            printf("\n");
        }
        printf("%c: %d\t", ch, (int)ch);
        ch_cnt++;
    }
    printf("\n");

    return 0;
}