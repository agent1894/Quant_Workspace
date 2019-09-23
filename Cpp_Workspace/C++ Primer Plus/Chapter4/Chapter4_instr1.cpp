// instr1.cpp -- reading more than one string
#include <iostream>

int main()
{
    using namespace std;

    const int ARSIZE = 20;
    char name[ARSIZE];
    char dessert[ARSIZE];

    cout << "Enter your name:" << endl;
    cin >> name;
    cout << "Enter your favourite dessert:" << endl;
    cin >> dessert;
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << endl;

    return 0;
}