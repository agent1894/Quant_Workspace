// 8.8.5 -- template function max5()
#include <iostream>
template <typename T>
T max5(T arr[5]);

int main()
{
    using namespace std;
    int arrInt[5] = {2, 3, 8, 1, 9};
    double arrDouble[5] =  {-3.4, 8.1, -76.4, 34.4, 2.4};
    cout << "The maximum value of the int array with 5 elements is: ";
    cout << max5(arrInt) << endl;
    cout << "The maximum value of the double array with 5 elements is: ";
    cout << max5(arrDouble) << endl;
    return 0;
}

template <typename T>
T max5(T arr[5])
{
    T tempMax = arr[0];
    for (int i = 0; i < 5; i++)
    {
        if (arr[i] > tempMax)
            tempMax = arr[i];
    }
    return tempMax;
}