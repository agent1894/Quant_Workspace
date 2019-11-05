// 5.9.6 -- using 2-D array for previous practice
#include <iostream>
#include <string>

int main()
{
    using namespace std;
    const int Years = 3;
    const int ArSize = 12;
    const string months[ArSize] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    int sales[Years][ArSize];
    for (int i = 0; i < Years; ++i)
    {
        cout << "Please enter the sales " << endl; 
        for (int j = 0; j < ArSize; ++j)
        {
            cout << "Year " << i + 1 << " sales";
            cout << " at month " << months[j] << "\t";
            cin >> sales[i][j];
        }
    }

    long cumsum = 0;
    for (int i = 0; i < Years; ++i)
    {
        for (int j = 0; j < ArSize; ++j)
            cumsum += sales[i][j];
    }
    cout << "The cumsum of 3 years sales are: " << cumsum << endl;

    return 0;
}