#include <stdio.h>

int main(void)
{
    double arr1 [8];
    double arr2 [8];
    for (int i = 0; i < 8; i++)
    {
        printf("Enter element %d in arr1: ", i + 1);
        scanf("%lf", &arr1[i]);
    }
    arr2[0] = arr1[0];
    for (int i = 1; i < 8; i++)
    {
        arr2[i] = arr2[i - 1] + arr1[i];
    }
    for (int i = 0; i < 8; i++)
    {
        printf("%10.4lf ", arr1[i]);
    }
    printf("\n");
    for (int i = 0; i < 8; i++)
    {
        printf("%10.4lf ", arr2[i]);
    }
    printf("\n");
}