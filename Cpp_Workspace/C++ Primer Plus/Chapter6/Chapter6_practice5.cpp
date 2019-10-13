// 6.11.5 -- Neutronia Kingdom taxes
#include <iostream>

int main()
{
    using namespace std;
    cout << "Enter the income (in hvarps) and get the taxes should pay. ";
    cout << "Enter negative or non-numeric to quit." << endl;
    double income;
    double taxes;
    while (cin >> income && income >= 0)
    {
        if (income <= 5000)
            taxes = 0;
        else if (income <= 15000)
            taxes = (income - 5000) * 0.1;
        else if (income <= 35000)
            taxes = (income - 15000) * 0.15 + 10000 * 0.1;
        else
            taxes = (income - 35000) * 0.2 + 10000 * 0.1 + 20000 * 0.15;
        cout << "The taxes you should pay is " << taxes << " tvarps." << endl;
        cout << "Enter the income (in hvarps) and get the taxes should pay. ";
        cout << "Enter negative or non-numeric to quit." << endl;
    }
    cout << "Thank you!" << endl;

    return 0;
}