// 5.9.3 -- cumsum of inputs
#include <iostream>

int main()
{
    using namespace std;

    double input;
    double cumsum = 0;

    cout << "Please enter a number and enter 0 to quit: ";
    cin >> input;
    while (input != 0)
    {
        cumsum += input;
        cout << "The cumsom of all inputs are: " << cumsum << endl;
        cout << "Please enter a number and enter 0 to quit: ";
        cin >> input;
    }

    return 0;
}