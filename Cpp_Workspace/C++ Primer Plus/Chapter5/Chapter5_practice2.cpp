// 5.9.2 -- using array to rewrite 5.4 formore.cpp
#include <iostream>
#include <array>

int main()
{
    using namespace std;

    const int ArSize = 101;
    array<long double, ArSize> factorials; // create array object of 100 long doubles
    factorials.at(0) = factorials.at(1) = 1.0; // array.at() check the index range, better than array[]

    for (int i = 2; i < ArSize; i++)
        factorials.at(i) = factorials.at(i-1) * i;

    cout << "100! = " << factorials.at(100) << endl;

    return 0;
}