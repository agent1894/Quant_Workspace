// 2.7.4 -- age into months
#include <iostream>

int main()
{
    using namespace std;

    cout << "Enter your age: ";
    int age;
    cin >> age;
    cout << "This age contains " << age * 12 << " months." << endl;

    return 0;
}