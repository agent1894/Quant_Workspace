// 3.7.6 -- miles per gallon (MPG)
#include <iostream>

int main()
{
    using namespace std;
    cout << "Enter the distances in miles: ";
    double miles;
    cin >> miles;
    cout << "Enter the oil consumption in gallon: ";
    double gallon;
    cin >> gallon;
    double mpg;
    mpg = miles / gallon;
    cout << "The MPG (miles per gallon) is " << mpg << "." << endl;

    return 0;
}