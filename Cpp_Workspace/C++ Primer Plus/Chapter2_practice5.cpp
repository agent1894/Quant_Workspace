// 2.7.5 -- convert Celsius degrees to Fahrenheit degrees
#include <iostream>
#include <cmath>

using namespace std;

double degree(double);

int main()
{
    cout << "Please enter a Celsius value: ";
    double Celsius;
    cin >> Celsius;
    cout << Celsius << " degrees Celsius is ";
    double Fahrenheit;
    Fahrenheit = degree(Celsius);
    cout << Fahrenheit << " degrees Fahrenheit." << endl;
    return 0;
}

double degree(double Celsius)
{
    double Fahrenheit;
    Fahrenheit = 1.8*Celsius + 32.0;
    return Fahrenheit;
}
