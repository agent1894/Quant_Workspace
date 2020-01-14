// 9.6.2 -- rewrite example 9.9
#include <iostream>
#include <string>
using namespace std;
void strcount(string str);

int main()
{
    cout << "Enter a line:\n";
    string str;
    getline(cin, str);
    while (str != "")
    {
        strcount(str);
        cout << "Enter next line (empty line to quit): \n";
        getline(cin, str);
    }
    cout << "Bye!\n";
    return 0;
}

void strcount(string str)
{
    static int total = 0;
    int count = str.size();

    cout << "\"" << str << "\" contains " << count << " characters\n";
    total += count;
    cout << total << " characters total\n";
}
