// textin2.cpp -- using cin.get(char)
#include <iostream>

int main()
{
    using namespace std;

    char ch;
    int count = 0; 
    cout << "Enter characters: enter # to quit: " << endl;
    cin.get(ch); // use the cin.get(ch) function
    while (ch != '#') // test the character
    {
        cout << ch;
        ++count;
        cin.get(ch); // use it again
    }
    cout << endl << count << " characters read" << endl;

    return 0;
    
}