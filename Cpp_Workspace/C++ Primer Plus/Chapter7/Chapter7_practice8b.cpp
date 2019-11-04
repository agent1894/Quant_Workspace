// 7.13.8b -- rewrite 7.15 by using structure
#include <iostream>

const int nSeason = 4;
const char* Seasons[20][nSeason] = {"Spring", "Summer", "Autumn", "Winter"};
struct exps
{
    double exp[nSeason];
};
void fill(exps* pt);
void show(exps expense);

int main()
{
    exps expense;
    fill(&expense);
    show(expense);

    return 0;
}

void fill(exps* pt)
{
    using namespace std;
    for (int i = 0; i < nSeason; i++)
    {
        cout << "Enter " << (*Seasons)[i] << " expenses: ";
        cin >> pt->exp[i];
    }
}

void show(exps expense)
{
    using namespace std;
    double total = 0.0;
    cout << "\nEXPENSES\n";
    for (int i = 0; i < nSeason; i++)
    {
        cout << (*Seasons)[i] << ": $" << expense.exp[i] << endl;
        total += expense.exp[i];
    }
    cout << "Total Expenses: $" << total << endl;
}