// 5.9.1 -- enter two integers
#include <iostream>

int main()
{
    using namespace std;

    int smaller, larger;
    cout << "Please enter the smaller integer: ";
    cin >> smaller;
    cout << "Please enter the larger integer: ";
    cin >> larger;
    for (int i = smaller + 1; i <= larger; ++i)
        smaller += i;
    cout << "The sum of two integers is: " <<  smaller << endl;

    return 0;
}