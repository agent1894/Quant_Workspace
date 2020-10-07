#include <stdio.h>

int main(void)
{
    const unsigned int TWO = 2;
    int in;
    unsigned int even_cnt = 0;
    unsigned int odd_cnt = 0;
    int even_sum = 0;
    int odd_sum = 0;
    float even_mean = 0;
    float odd_mean = 0;
    printf("Enter intergers with 0 to stop.\n");
    while (scanf("%d", &in) == 1 && in != 0)
    {
        if (in % TWO == 0)
        {
            even_cnt++;
            even_sum += in;
        }
        else
        {
            odd_cnt++;
            odd_sum += in;
        }
    }
    even_mean = even_sum / (float)even_cnt;
    odd_mean = odd_sum / (float)odd_cnt;

    printf("The count of even integers is %d, and the mean of these integers is %f.\n", even_cnt, even_mean);
    printf("The count of odd integers is %d, and the mean of these integers is %f.\n", odd_cnt, odd_mean);

    return 0;
}