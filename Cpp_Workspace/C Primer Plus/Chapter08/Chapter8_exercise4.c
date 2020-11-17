#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int main(void)
{
    float average = 0;
    unsigned int word_count = 0;
    unsigned int letter_count = 0;
    bool new_word = true;
    char ch;

    printf("Enter a sentense:\n");
    while ((ch = getchar()) != EOF)
    {
        if (ispunct(ch))
        {
            continue;
        }
        else if (isspace(ch))
        {
            new_word = true;
            continue;
        }
        else
        {
            letter_count++;
            if (new_word)
            {
                word_count++;
                new_word = false;
            }
        }
    }
    average = (float)letter_count / word_count;

    printf("This sentense has %d words with average %.2f letters length.\n", word_count, average);

    return 0;
}