// 7.13.8a -- rewrite 7.15 by avoiding use the array class
#include <iostream>

const int nSeason = 4;
const char* Seasons[20][nSeason] = {"Spring", "Summer", "Autumn", "Winter"};
void fill(double expenses[]);
void show(double expenses[]);

int main()
{
    double expenses[nSeason];
    fill(expenses);
    show(expenses);

    return 0;
}

void fill(double expenses[])
{
    using namespace std;
    for (int i = 0; i < nSeason; i++) 
    {
        cout << "Enter " << (*Seasons)[i] << " expenses: ";
        cin >> expenses[i];
    }
}

void show(double expenses[])
{
    using namespace std;
    double total = 0.0;
    cout << "\nEXPENSES\n";
    for (int i = 0; i < nSeason; i++)
    {
        cout << (*Seasons)[i] << ": $" << expenses[i] << endl;
        total += expenses[i];
    }
    cout << "Total Expenses: $" << total << endl;
}