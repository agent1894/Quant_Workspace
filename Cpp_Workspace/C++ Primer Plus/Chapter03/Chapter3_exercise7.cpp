// 3.7.7 -- distance & fuel
#include <iostream>

int main()
{
    using namespace std;

    cout << "Enter European style automobile fuel costs (liters/100km): ";
    double liters;
    cin >> liters;

    const double MILE = 62.14;
    const double GALLON = 3.875;

    int mpg = 1.0 / (liters / MILE / GALLON);
    cout << "Convert into the US mpg: " << mpg << endl;

    return 0;
}