// and.cpp -- using the logical AND operator
#include <iostream>
const int ArSize = 6;
int main()
{
    using namespace std;

    float naaq[ArSize];
    cout << "Enter the NAAQs (New Age Awareness Quotients) ";
    cout << "of\nyour neighbours. Program terminates ";
    cout << "when you make\n" << ArSize << " entries ";
    cout << "or enter a negative value." << endl;

    int i = 0;
    float temp;
    cout << "First value: ";
    cin >> temp;
    while (i < ArSize && temp >= 0) // 2 quitting criteria
    {
        naaq[i] = temp;
        ++i;
        if (i < ArSize) // room left in the array
        {
            cout << "Next value: ";
            cin >> temp; // so get next value
        }
    }
    if (i == 0)
        cout << "No data--bye" << endl;
    else
    {
        cout << "Enter your NAAQ: ";
        float you;
        cin >> you;
        int count = 0;
        for (int j = 0; j < i; j++)
            if (naaq[j] > you)
                ++count;
        cout << count;
        cout << " of your neighbours have greater awareness of " << endl;
        cout << "the New Age than you do." << endl;
    }

    return 0;
}