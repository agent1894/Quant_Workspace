// 4.13.4 -- input name using string
#include <iostream>
#include <string>
#include <cstring>

int main()
{
    using namespace std;

    string firstName;
    string lastName;
    cout << "Enter your first name: ";
    cin >> firstName;
    cout << "Enter your last name: ";
    cin >> lastName;
    string fullName;
    fullName = lastName + ", " + firstName;
    cout << "Here's the information in a single string: " << fullName << endl;

    return 0;
}