// ourfunc.cpp -- defining your own function
#include <iostream>

using namespace std;

void simon(int); // function prototype

int main()
{
    simon(3);
    cout << "Pick an integer: ";
    int count;
    cin >> count;
    simon(count);
    cout << "Done!" << endl;
    return 0;
}

void simon(int n)
{
    cout << "Simon says touch your toes " << n << " times." << endl;
} // void function has nothing to return