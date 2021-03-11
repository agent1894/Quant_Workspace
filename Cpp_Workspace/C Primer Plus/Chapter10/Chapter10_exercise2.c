#include <stdio.h>
#define LEN 5
void copy_arr(double target[], double const source[], int num);
void copy_ptr(double *target, double const *source, int num);
void copy_ptrs(double *target, double const *source, double const *pos);
void show_arr(double const ar[]);

int main(void)
{
    double source[5] = {1.1, 2.2, 3.3, 4.4, 5.5};
    double target1[5];
    double target2[5];
    double target3[5];

    printf("source array:\n");
    for (int i = 0; i < LEN; ++i)
    {
        printf("%f ", source[i]);
    }
    printf("\n\n");

    copy_arr(target1, source, 5);
    copy_ptr(target2, source, 5);
    copy_ptrs(target3, source, source + 5);

    return 0;
}

void copy_arr(double target[], double const source[], int num)
{
    int i;
    for (i = 0; i < num; ++i)
    {
        target[i] = source[i];
    }
    printf("copy1 array:\n");
    show_arr(target);
}

void copy_ptr(double *target, double const *source, int num)
{
    int i;
    for (i = 0; i < num; ++i)
    {
        *(target + i) = *(source + i);
    }
    printf("copy2 array:\n");
    show_arr(target);
}

void copy_ptrs(double *target, double const *source, double const *pos)
{
    double *ptr = target;
    while (source < pos)
    {
        *ptr = *source;
        ptr++;
        source++;
    }
    printf("copy3 array:\n");
    show_arr(target);
}

void show_arr(double const ar[])
{
    int i;
    for (i = 0; i < LEN; ++i)
    {
        printf("%f ", ar[i]);
    }
    putchar('\n');
}