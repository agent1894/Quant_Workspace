// dowhile.cpp -- exit-condition loop
#include <iostream>

int main()
{
    using namespace std;
    int n;

    cout << "Enter numbers in the range 1-10 to find ";
    cout << "my favourite number" << endl;
    do
    {
        cin >> n; // execute body
    } while (n != 7); // then test
    cout << "Yes, 7 is my favourite." << endl;

    return 0;
}