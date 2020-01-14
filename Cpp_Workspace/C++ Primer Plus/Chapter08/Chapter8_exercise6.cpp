// 8.8.6 -- template function maxn()
#include <iostream>
#include <cstring>

template<typename T>
T maxn(T arr[], int n);
template <>
const char* maxn<const char*>(const char* arr[], int n);

int main()
{
    using namespace std;
    int arrInt[6] = {2, 3, 81, 1, 9, 22};
    double arrDouble[4] = {-3.4, 58.1, -76.4, 34.4};
    const char * arrStr[5] = {"Here", "is", "a", "test", "sequence"};
    cout << "The maximum value of the int array is: ";
    cout << maxn(arrInt, 6) << endl;
    cout << "The maximum value of the double array is: ";
    cout << maxn(arrDouble, 4) << endl;
    cout << "The longest string is: ";
    cout << maxn(arrStr, 5) << endl;
    return 0;
}

template<typename T>
T maxn(T arr[], int n)
{
    T tempMax = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] > tempMax)
            tempMax = arr[i];
    }
    return tempMax;
}

template <>
const char* maxn<const char*>(const char* arr[], int n)
{
    using namespace std;
    unsigned int maxLength = 0;
    int index = 0;
    for (int i = 0; i < n; i++)
    {
        if (strlen(arr[i]) > maxLength)
        {
            maxLength = strlen(arr[i]);
            index = i;
        }
    }
    return arr[index];
}