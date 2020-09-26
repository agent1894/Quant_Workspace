#include <stdio.h>

int main(void)
{
    int age;
    double SECONDS = 3.156E7;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Age is approximately %e seconds.\n", age * SECONDS);

    return 0;
}