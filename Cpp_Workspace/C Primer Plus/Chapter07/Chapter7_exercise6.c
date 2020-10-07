#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    char ch;
    bool flag = false;
    unsigned int cnt = 0;
    printf("Enter a sentence with # to stop.\n");
    while ((ch = getchar()) != '#')
    {
        if (ch == 'e')
        {
            flag = true;
        }
        else if (ch == 'i')
        {
            if (flag)
            {
                cnt++;
            }
            flag = false;
        }
        else
        {
            flag = false;
        }
    }

    printf("'ei' occurs %d times.\n", cnt);

    return 0;
}