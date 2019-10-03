// 5.9.5 -- selling <C++ For Fools>
#include <iostream>
#include <string>

int main()
{
    using namespace std;
    int ArSize = 12;
    const string months[ArSize] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    int sales[ArSize];
    for (int i = 0; i < ArSize; ++i)
    {
        cout << "Please enter the volume of sales in month: " << months[i] << endl;
        cin >> sales[i];
    }

    long totalSales = 0;
    for (int i = 0; i < ArSize; ++i)
        totalSales += sales[i];

    cout << "The total sales are: " << totalSales << endl;

    return 0;
}