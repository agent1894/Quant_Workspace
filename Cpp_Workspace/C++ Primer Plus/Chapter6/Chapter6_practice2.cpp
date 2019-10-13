// 6.11.2 -- count donation
#include <iostream>

int main()
{
    using namespace std;
    int i = 0;
    int Max = 10;
    double donation[Max];
    cout << "Please enter the donation: " << endl;
    cout << "Donation #" << i + 1 << ": $";
    while (i < Max && cin >> donation[i])
    {
        if (++i < Max)
            cout << "Donation #" << i + 1 << ": $";
    }
    double sum = 0.0;
    for (int j = 0; j < i; ++j)
        sum += donation[j];
    double mean = sum / i;
    cout << "The average donation is: $" << mean << endl;
    int aboveMean = 0;
    for (int j = 0; j < i; ++j)
    {
        if (donation[j] > mean)
            aboveMean++;
    }
    cout << "There is(are) " << aboveMean << " donation(s) larger than the average donation." << endl;

    return 0;
}