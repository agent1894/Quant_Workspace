// floatnum.cpp -- floating-point types
#include <iostream>

using namespace std;

int main()
{
    cout.setf(ios_base::fixed, ios_base::floatfield);
    float tub = 10.0/3.0;
    double mint = 10.0/3.0;
    const float MILLION = 1.0e6;

    cout << "tub = " << tub;
    cout << ", a million tubs = " << MILLION * tub;
    cout << "\nand ten million tubs = ";
    cout << 10 * MILLION * tub << endl;

    cout << "mint = " << mint << " and a million mints = ";
    cout << MILLION * mint << endl;

    return 0;
}