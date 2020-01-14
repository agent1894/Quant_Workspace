// strtype4.cpp -- line input
#include <iostream>
#include <string>
#include <cstring>

int main()
{
    using namespace std;

    char charr[20];
    string str;

    cout << "Length of string in charr before input: ";
    cout << strlen(charr) << endl;

    cout << "Length of string in str before input: ";
    cout << str.size() << endl;

    cout << "Enter a line of text" << endl;
    cin.getline(charr, 20); // indicate maximum length
    cout << "You entered: " << charr << endl;
    cout << "Enter another line of text: " << endl;
    getline(cin, str); // cin now an argument; no length specifier
    cout << "You entered: " << str << endl;
    cout << "Length of string in charr after input: ";
    cout << strlen(charr) << endl;
    cout << "Lenght of string in str after input: ";
    cout << str.size() << endl;

    return 0;
}