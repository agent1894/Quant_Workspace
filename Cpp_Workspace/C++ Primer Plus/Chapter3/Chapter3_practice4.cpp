// 3.7.4 -- number of seconds
#include <iostream>
#include <climits>

int main()
{
    using namespace std;

    const int Seconds_perMinute = 60;
    const int Seconds_perHour = 3600;
    const int Seconds_perDay = 86400;
    cout << "Enter the number of seconds: ";
    long long enter_seconds;
    cin >> enter_seconds;
    int days, hours, minutes, seconds;
    days = enter_seconds / Seconds_perDay;
    hours = enter_seconds % Seconds_perDay / Seconds_perHour;
    minutes = enter_seconds % Seconds_perDay % Seconds_perHour / Seconds_perMinute;
    seconds = enter_seconds % Seconds_perDay % Seconds_perHour % Seconds_perMinute; 

    cout << enter_seconds << " seconds = " << days << " days, ";
    cout << hours << " hours, ";
    cout << minutes << " minutes, ";
    cout << seconds << " seconds." << endl;

    return 0;
}