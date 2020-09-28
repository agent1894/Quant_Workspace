#include <stdio.h>

int main(void)
{
    int arr [8];
    int idx = 0;
    arr[0] = 2;

    for (int i = 1; i < 8; i++)
    {
        arr[i] = 2 * arr[i - 1];
    }
    do
    {
        printf("%d ", arr[idx]);
        idx++;
    } while (idx < 8);
    printf("\n");
    
    return 0;
}