// 4.13.3 -- input name
#include <iostream>
#include <string>
#include <cstring>

int main()
{
    using namespace std;

    char firstName[30];
    char lastName[30];
    cout << "Enter your first name: ";
    cin >> firstName;
    cout << "Enter your last name: ";
    cin >> lastName;
    string fullName;
    const char sep[] = ", ";
    fullName = strcat(strcat(lastName, sep), firstName);
    cout << "Here's the information in a single string: " << fullName << endl;

    return 0;
}