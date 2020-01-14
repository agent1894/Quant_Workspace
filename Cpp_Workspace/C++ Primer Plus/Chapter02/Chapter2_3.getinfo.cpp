// getinfo.cpp -- input and output
#include <iostream>
using namespace std;

int main()
{
    int carrots;
    cout << "How many carrots do you have?" << endl;
    cin >> carrots;
    cout << "Here are two more. ";
    cout << "Now you have " << carrots+2 << " carrots." << endl;

    return 0;
}