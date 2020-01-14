// 4.13.10 -- Array of race records
#include <iostream>
#include <array>
#include <cmath>

int main()
{
    using namespace std;
    array<double, 3> records;
    cout << "Please enter the first record: ";
    cin >> records[0];
    cout << "Please enter the second records: ";
    cin >> records[1];
    cout << "Please enter the last records: ";
    cin >> records[2];

    cout << "The average record of 3 times is: " << (records[0] + records[1] + records[2])/3.0 << endl;

    return 0;
}