// convert.cpp -- converts stone to pounds
#include <iostream>
using namespace std;

int stonetolb(int); //function prototype

int main()
{
    cout << "Enter the weight in stone: ";
    int stone;
    cin >> stone;
    int pounds;
    pounds = stonetolb(stone);
    cout << stone << " stone = " << pounds << " pounds." << endl;

    return 0;
}

int stonetolb(int sts)
{
    // return 14*sts;
    int pounds;
    pounds = 14*sts;
    return pounds;
}