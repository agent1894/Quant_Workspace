// 3.7.1 -- convert height
#include <iostream>

int main()
{
    using namespace std;
    const int conversion = 12;
    cout << "Enter the height in integer inches: ___\b\b\b";
    int height;
    cin >> height;
    int feet, inch;
    feet = height / conversion;
    inch = height % conversion;
    cout << "You are " << feet << " feet and " << inch << " inches height. " << endl;

    return 0;
}