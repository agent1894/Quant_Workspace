#include <stdio.h>

int main(void)
{
    int lower_bound;
    int upper_bound;
    printf("lower bound: ");
    scanf("%d", &lower_bound);
    printf("upper bound: ");
    scanf("%d", &upper_bound);
    printf("%8s, %8s, %8s\n", "num", "square", "cube");
    for (int i = lower_bound; i < upper_bound + 1; i++)
    {
        printf("%*d, %*d, %*d\n", 8, i, 8, i * i, 8, i * i * i);
    }

    return 0;
}