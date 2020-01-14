// cinfish.cpp -- non-numeric input terminates loop
#include <iostream>
const int Max = 5;
int main()
{
    using namespace std;
    // get data
    double fish[Max];
    cout << "Please enter the weights of your fish. " << endl;
    cout << "You may enter up to " << Max << " fish <q to terminates." << endl;
    cout << "fish #1: ";
    int i = 0;
    while (i < Max && cin >> fish[i])
    {
        if (++i < Max)
            cout << "fish #" << i+1 << ": ";
    }
    // calcualte average
    double total = 0.0;
    for (int j = 0 ; j < i; j++)
        total += fish[j];
    // report results
    if  (i == 0)
        cout << "No fish" << endl;
    else
        cout << total / i << " = average weight of " << i << "fish" << endl;
    cout << "Done" << endl;

    return 0;
}