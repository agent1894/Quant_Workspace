// numstr.cpp -- following number input with line input
#include <iostream>

int main()
{
    using namespace std;

    cout << "What year was your house built? " << endl;
    int year;
    cin >> year;
    // FIX:
    cin.get(); // or cin.get(ch);
    // or:
    //(cin >> year).get(); // or (cin >> year).get(ch)
    cout << "What is its street address? " << endl;
    char address[80];
    cin.getline(address, 80);
    cout << "Year built: " << year << endl;
    cout << "Address: " << address << endl;
    cout << "Done!" << endl;

    return 0;
}