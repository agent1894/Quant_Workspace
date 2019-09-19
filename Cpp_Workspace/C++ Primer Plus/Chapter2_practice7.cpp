// 2.7.7 -- input Hours/Minutes and output time
#include <iostream>
#include <cmath>

using namespace std;

void format(int, int);

int main()
{
    cout << "Enter the number of hours: ";
    int hours;
    cin >> hours;
    cout << "Enter the number of minutes: ";
    int minutes;
    cin >> minutes;
    format(hours, minutes);

    return 0;
}

void format(int hours, int minutes)
{
    cout << "Time: " << hours << ":" << minutes << endl;
}