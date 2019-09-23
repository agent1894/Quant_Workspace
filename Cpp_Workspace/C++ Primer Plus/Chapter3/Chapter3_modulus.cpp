// modulus.cpp -- use % operator to convert lbs to stone
#include <iostream>

int main()
{
    using namespace std;

    const int Lbs_per_stn = 14;

    cout << "Enter your weight in pounds: ";
    int lbs;
    cin >> lbs;
    int stone = lbs / Lbs_per_stn; // whole stone
    int pounds = lbs % Lbs_per_stn; // remainder in pounds
    cout << lbs << " pounds are " << stone;
    cout << " stone, " << pounds << " pound(s)." << endl;

    return 0;
}