// 5.9.7 -- information about cars
#include <iostream>
#include <string>
using namespace std;

struct car
{
    string manufacturer;
    int produceYear;
};

int main()
{
    int number;
    cout << "How many cars do you wish to catalog? ";
    cin >> number;
    cin.get();
    car * cars = new car[number]; // dynamic binding
    for (int i = 0; i < number; ++i)
    {
        cout << "Car #" << i + 1 << ": " << endl;
        cout << "Please enter the make: ";
        getline(cin, cars[i].manufacturer);
        cout << "Please enter the year made: ";
        cin >> cars[i].produceYear;
        cin.get();
    }
    cout << "Here is your collection: " << endl;
    for (int i = 0; i < number; i++)
        cout << cars[i].produceYear << " " << cars[i].manufacturer << endl;

    delete [] cars; // free memory when finished

    return 0;
}