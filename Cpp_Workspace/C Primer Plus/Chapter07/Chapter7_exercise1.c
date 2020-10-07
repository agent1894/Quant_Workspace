#include <stdio.h>

int main(void)
{
    char ch;
    unsigned int space_cnt = 0;
    unsigned int return_cnt = 0;
    unsigned int other_cnt = 0;
    printf("Enter a sentence with # to stop.\n");
    while ((ch = getchar()) != '#')
    {
        if (ch == ' ')
        {
            space_cnt++;
        }
        else if (ch == '\n')
        {
            return_cnt++;
        }
        else
        {
            other_cnt++;
        }
    }
    printf("This sentence has %d spaces, %d returns and %d other characters.\n", space_cnt, return_cnt, other_cnt);

    return 0;
}