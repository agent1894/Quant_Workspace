// instr2.cpp -- reading more than one word with genline
#include <iostream>

int main()
{
    using namespace std;

    const int ARSIZE = 20;
    char name[ARSIZE];
    char dessert[ARSIZE];

    cout << "Enter your name: " << endl;
    cin.getline(name,ARSIZE); // reads through newline
    cout << "Enter your favourite dessert: " << endl;
    cin.getline(dessert,ARSIZE);
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << ".\n";

    return 0;
}