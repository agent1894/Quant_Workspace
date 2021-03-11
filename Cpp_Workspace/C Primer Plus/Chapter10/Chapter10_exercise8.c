#include <stdio.h>
#define LEN 7
void copy_ptr(double *target, double const *source, int const num);
void show_arr(double const *ar, int const num);

int main(void)
{
    int size = 3;
    int start = 2;
    double source[LEN] = {2.4, -6.4, 5.0, 2.7, 3.6, 1.1, 8.9};
    double target[size];

    printf("Source array is:\n");
    show_arr(source, LEN);
    printf("Copy from element %d to element %d in source array to target array. ", start + 1, start + size);
    copy_ptr(target, source + start, size);
    printf("Target array is:\n");
    show_arr(target, size);

    return 0;
}

void copy_ptr(double *target, double const *source, int const num)
{
    int i;

    for (i = 0; i < num; ++i)
    {
        *(target + i) = *(source + i);
    }
}

void show_arr(double const *ar, int const num)
{
    int i;

    for (i = 0; i < num; ++i)
    {
        printf("%.2f ", *(ar + i));
    }
    putchar('\n');
}