// instr3.cpp -- reading more than one word with get() & get()
#include <iostream>

int main()
{
    using namespace std;

    const int ARSIZE = 20;
    char name[ARSIZE];
    char dessert[ARSIZE];

    cout << "Enter your name: " << endl;
    cin.get(name,ARSIZE).get(); // read string, newline
    cout << "Enter your favourite dessert: " << endl;
    cin.get(dessert,ARSIZE).get();
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << ".\n";

    return 0;
}