#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char ch;
    unsigned int upper = 0;
    unsigned int lower = 0;
    unsigned int other = 0;
    printf("Enter a sentense:\n");
    while ((ch = getchar()) != EOF)
    {
        if (isalpha(ch))
        {
            if (isupper(ch))
            {
                upper++;
            }
            else
            {
                lower++;
            }
            
        }
        else
        {
            other++;
        }
    }
    printf("The string has %d upper characters, %d lower characters and %d other characters.\n", upper, lower, other);

    return 0;
}