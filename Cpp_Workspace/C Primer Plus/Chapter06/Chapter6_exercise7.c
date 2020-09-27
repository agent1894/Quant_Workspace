#include <stdio.h>
#include <string.h>

int main(void)
{
    char str [20];
    int length;
    printf("Enter a word: ");
    scanf("%s", str);
    length = strlen(str);
    printf("The reverse of the word is: ");
    for (int i = length - 1; i >= 0; i--)
    {
        printf("%c", str[i]);
    }
    printf("\n");

    return 0;
}