// 2.7.6 -- convert light years to astronomical units
#include <iostream>
#include <cmath>

using namespace std;

double astronomical(double);

int main()
{
    cout << "Enter the number of light years: ";
    double years;
    cin >> years;
    double units;
    units = astronomical(years);
    cout << years << " light years = " << units << " astronomical units." << endl;

    return 0;
}

double astronomical(double years)
{
    return 63240 * years;
}
