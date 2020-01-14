// 5.9.4 -- value of investments, simple interest vs compound interest
#include <iostream>

int main()
{
    using namespace std;
    long double daphne = 100;
    long double cleo = 100;
    int year = 0;

    while (daphne >= cleo)
    {
        daphne += 10;
        cleo *= 1.05;
        year++;
    }
    cout << "At the year of " << year << endl;
    cout << "Daphne has $" << daphne;
    cout << " and Cleo has $" << cleo << endl;

    return 0;
}