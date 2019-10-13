// 6.11.6 -- donation funds
#include <iostream>
#include <string>

struct patron
{
    std::string name;
    double money;
};

int main()
{
    using namespace std;
    cout << "Enter the number of patrons: ";
    int number;
    cin >> number;    
    cin.get();
    patron * patrons = new patron[number];
    for (int i = 0; i < number; ++i)
    {
        cout << "Patron #" << i + 1 << ": " << endl;
        cout << "Please enter the name: ";
        getline(cin, patrons[i].name);
        cout << "Please enter the amount of donation : $";
        cin >> patrons[i].money;
        cin.get();
    }
    cout << "Grand Patrons: " << endl;
    int count = 0;
    for (int i = 0; i < number; ++i)
    {
        if (patrons[i].money >= 10000)
        {
            cout << patrons[i].name << ": $" << patrons[i].money << '\t';
            ++count;
        }
    }
    if (count == 0)
        cout << "None" << endl;
    else
        cout << endl;
    cout << "Patrons: " << endl;
    count = 0;
    for (int i = 0; i < number; ++i)
    {
        if (patrons[i].money < 10000)
        {
            cout << patrons[i].name << '\t';
            ++count;
        }
    }
    if (count == 0)
        cout << "None" << endl;
    else
        cout << endl;

    delete [] patrons;
    return 0;
}