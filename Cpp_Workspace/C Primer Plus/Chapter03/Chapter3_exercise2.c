#include <stdio.h>

int main(void)
{
    int ascii;
    printf("Enter a ASCII: ");
    scanf("%d", &ascii);
    printf("The ASCII code for %c is %d\n", ascii, ascii);

    return 0;
}