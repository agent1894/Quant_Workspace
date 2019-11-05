// or.cpp -- using the logical OR operator
#include <iostream>

int main()
{
    using namespace std;

    cout << "This program may reformat your hard disk" << endl;
    cout << "and destory all your data." << endl;
    cout << "Do you wish to continue? <y/n> ";

    char ch;
    cin >> ch;
    if (ch == 'y' || ch == 'Y') // y or Y
        cout << "You were warned!\a\a\n";
    else if (ch == 'n' || ch == 'N') // n or N
        cout << "A wise choice ... bye" << endl;
    else
    {
        cout << "That wasn't a y or n! Apparently you ";
        cout << "can't follow\ninstructions, so ";
        cout << "I'll trash your disk anyway. \a\a\a" << endl;
    }

    return 0;
}