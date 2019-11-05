// 7.13.10 -- function calcualte() with function pointers
#include <iostream>
#include <cmath>
#include <string>

double calculate(double x, double y, double (*pt)(double a, double b));
double add(double x, double y);
double arithmeticMean(double x, double y);
double geometricMean(double x, double y);

int main()
{
    using namespace std;
    const int Funcs = 3;
    string funcNames[Funcs] = {"Add", "Arithmetic Mean", "Geometric Mean"};
    double (*pf[3])(double, double) = {add, arithmeticMean, geometricMean};
    double x, y;
    cout << "Enter two double values (q to quit): ";
    while (cin >> x >> y)
    {
        // use function's name
        cout << "The add function returns: ";
        cout << calculate(x, y, add) << endl;
        cout << "The arithmetic mean function returns: ";
        cout << calculate(x, y, arithmeticMean) << endl;
        cout << "The geometric mean function returns: ";
        cout << calculate(x, y, geometricMean) << endl;
        // use the pointer array
        for (int i = 0; i < Funcs; i++)
        {
            cout << "The " << funcNames[i] << " of inputs = ";
            cout << calculate(x, y, pf[i]) << endl;
        }
        cout << "Enter two double values (q to quit): ";
    }
    cout << "Done!" << endl;

    return 0;
}

double calculate(double x, double y, double (*pt)(double a, double b))
{
    return (*pt)(x, y);
}

double add(double x, double y)
{
    return x + y;
}

double arithmeticMean(double x, double y)
{
    return (x + y) / 2.0;
}

double geometricMean(double x, double y)
{
    return std::sqrt(x * y);
}