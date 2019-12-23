// 8.8.4 -- complete function
#include <iostream>
using namespace std;
#include <cstring> // for strlen(), strcpy()
struct stringy
{
    char* str; // points to a string
    int ct; // length of string (not counting '\0')
};

void set(stringy& stry, const char* str);
void show(stringy& stry, int times = 1);
void show(const char* str, int times = 1);

int main()
{
    stringy beany;
    char testing[] = "Reality isn't what is used to be.";

    
    set(beany, testing); // first argument is a reference, 
        // allocates space to hold copy of testing,
        // sets str member of beany to point to the new block,
        // copies testing to new block, 
        // and sets ct member of beany
    show(beany); // prints member string once
    show(beany, 2); // prints member string twice
    testing[0] = 'D';
    testing[1] = 'u';
    show(testing); // prints testing string once
    show(testing, 3); // prints testing string thrice
    show("Done!");
    return 0;
}

void set(stringy& stry, const char* str)
{
    stry.ct = strlen(str);
    stry.str = new char[stry.ct + 1];
    strcpy(stry.str, str);
}

void show(stringy& stry, int times)
{
    for (int i = 0; i < times; i++)
        cout << stry.str << ' ';
    cout << endl;
}

void show(const char* str, int times)
{
    for (int i = 0; i < times; i++)
        cout << str << ' ';
    cout << endl;
}