#include <stdio.h>

float user_func(float x, float y);

int main(void)
{
    int num;
    float x, y;
    float result;
    printf("Enter a pair of floats: ");
    num = scanf("%f %f", &x, &y);
    while (num == 2)
    {
        result = user_func(x, y);
        printf("(X - Y) / (X * Y) = %f\n", result);
        printf("Enter a new pair of floats: ");
        num = scanf("%f %f", &x, &y);
    }
    
    printf("Done\n");

    return 0;
}

float user_func(float x, float y)
{
    return (x - y) / (x * y);
}