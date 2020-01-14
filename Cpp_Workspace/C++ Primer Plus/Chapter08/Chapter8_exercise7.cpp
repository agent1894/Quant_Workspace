// 8.8.7 -- rewrite 8.14
#include <iostream>
// 使其使用两个名为SumArray()的模板函数来返回数组元素的综合，而不是显示数组的内容。程序应显示thing的总和以及所有debt的总和
using namespace std;
template <typename T>
T SumArray(T arr[], int len);

template <typename T>
T SumArray(T* arr[], int len);

struct debts
{
    char name[50];
    double amount;
};

int main()
{
    int things[6] = {13, 31, 103, 301, 310, 130};
    struct debts mr_E[3] = 
    {
        {"Ima Wolfe", 2400.0},
        {"Ura Foxe", 1300.0},
        {"Iby Stout", 1800.0}
    };
    double * pd[3];
    for (int i = 0; i < 3; i++)
        pd[i] = &mr_E[i].amount;
    cout << "The sum of Mr. E's things: ";
    cout << SumArray(things, 6) << endl;
    cout << "The sum of Mr. E's debts: ";
    cout << SumArray(pd, 3) << endl;
    return 0;
}

template <typename T>
T SumArray(T arr[], int len)
{
    T sum = arr[0];
    for (int i = 1; i < len; i++)
        sum += arr[i];
    return sum;
}

template <typename T>
T SumArray(T* arr[], int len)
{
    T sum = *arr[0];
    for (int i = 1; i < len; i++)
        sum += *arr[i];
    return sum;
}