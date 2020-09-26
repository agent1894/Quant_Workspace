#include <stdio.h>

int main(void)
{
    char name [20];
    float height;
    printf("Enter the name: ");
    scanf("%s", name);
    printf("Enter the height (in cm): ");
    scanf("%f", &height);
    printf("%s, you are %4.3f m tall\n", name, height / 100.0);

    return 0;
}