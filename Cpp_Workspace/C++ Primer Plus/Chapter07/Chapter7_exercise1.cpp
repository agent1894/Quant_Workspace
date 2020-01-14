// 7.13.1 -- harmonic mean
#include <iostream>
double harmonicMean(double x, double y);

int main()
{
    using namespace std;
    cout << "Please enter two numbers (0 to quit): " << endl;
    double x, y;
    while (cin >> x >> y && x != 0 && y != 0)
    {
        cout << "The harmonic mean is: ";
        cout << harmonicMean(x, y) << endl;
    }
    cout << "Done!" << endl;

    return 0;
}

double harmonicMean(double x, double y)
{
    return 2.0 * x * y / (x + y);
}