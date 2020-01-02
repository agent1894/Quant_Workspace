#include <iostream>
#include "Chapter9_exercise1.golf.h"

int main()
{
    using namespace std;
    cout << "Start program, enter empty line to stop inputting." << endl;
    golf user;
    int result = 1;
    while (result)
    {
        result = setgolf(user);
        showgolf(user);
    }
    cout << "Now change " << user.fullname << "'s handicap: ";
    int newHC;
    cin >> newHC;
    handicap(user, newHC);
    showgolf(user);
    return 0;
}