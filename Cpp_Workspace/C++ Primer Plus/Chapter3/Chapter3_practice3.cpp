// 3.7.3 -- latitude in degrees, minutes, and seconds
#include <iostream>
#include <climits>

int main()
{
    using namespace std;
    
    const int CONVERT = 60;
    cout << "Enter a latitude in degrees, minutes, and seconds: " << endl;
    int degrees, minutes, seconds;
    cout << "First, enter the degrees: ";
    cin >> degrees;
    cout << "Next, enter the minutes of arc: ";
    cin >> minutes;
    cout << "Finally, enter the seconds of arc: ";
    cin >> seconds;

    double converts = double(degrees) + double(minutes) / CONVERT + double(seconds) / CONVERT / CONVERT;
    cout << degrees << " degrees, " << minutes << " minutes, " << seconds << " seconds = ";
    cout << converts << " degrees" << endl;

    return 0;
}