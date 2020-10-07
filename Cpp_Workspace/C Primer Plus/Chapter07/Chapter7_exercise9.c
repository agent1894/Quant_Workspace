#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(unsigned int x);


int main(void)
{
    unsigned int input;
    printf("Enter a positive integer:");
    scanf("%d", &input);
    printf("The prime numbers less or equal than given integer are:\n");
    for (int i = 1; i <= input; ++i)
    {
        if (is_prime(i))
        {
            printf("%d ", i);
        }
    }
    printf("\n"); 
    return 0;
}

bool is_prime(unsigned int x)
{
    double square_root;
    square_root = sqrt((double)x);
    for (int i = 2; i <= square_root; ++i)
    {
        if (x % i == 0)
        {
            return false;
        }
    }
    return true;
}