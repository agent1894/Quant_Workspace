// bondini.cpp -- using escape sequences
#include <iostream>

using namespace std;

int main()
{
    cout << "\aOperation \"HyperType\" is now activated! \n";
    cout << "Enter your agent code:________\b\b\b\b\b\b\b\b"; // \b退格在不同编译器中的表现不尽相同
    long code;
    cin >> code;
    cout << "\aYou entered " << code << "...\n";
    cout << "\aCode verified! Proceed with plan Z3!" << endl;

    return 0;
}