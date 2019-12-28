// 8.8.1 -- accept parameters
#include <iostream>
void print(const char * str, int times = 0);
using namespace std;

int main()
{
    cout << "Please enter the string: ";
    const int Size = 80;
    char str[Size];
    cin.getline(str, Size);
    int times;
    cout << "Please enter the print times: ";
    cin >> times;
    if (times == 0)
        print(str);
    else
        for (int i = 0; i < times; i++)
            print(str, times);

    return 0;
}

void print(const char * str, int times)
{
    if (times == 0)
        cout << str << endl;
    for (int i = 0; i < times; i++)
        cout << str << ' ';
    cout << endl;
}