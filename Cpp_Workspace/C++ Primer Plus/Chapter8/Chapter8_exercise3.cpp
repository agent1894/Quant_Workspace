// 8.8.3 -- case switch
#include <iostream>
#include <string>
#include <cstring>
#include <cctype>
using namespace std;

void caseSwitch(string& str);

int main()
{
    cout << "Enter a string (q to quit): ";
    string str;
    while (getline(cin, str) && str != "q")
    {
        caseSwitch(str);
        cout << str << endl;
        cout << "Next string (q to quit): ";
    }
    cout << "Bye." << endl;
    return 0;
}

void caseSwitch(string& str)
{
    for (unsigned int i = 0; i < str.size(); i++)
        str[i] = toupper(str[i]);
}