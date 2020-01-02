// 9.6.3 -- placement new
#include <iostream>
#include <new>
#include <cstring>

struct chaff
{
    char dross[20];
    int slag;
};

int main()
{
    using namespace std;
    chaff* pt;
    char* buffer = new char[100];
    pt = new(buffer) chaff[2];
    for (int i = 0; i < 2; i++)
    {
        cout << "Please enter the " << i + 1 << " dross: ";
        char tempChar[20];
        cin.getline(tempChar, 20);
        strcpy(pt[i].dross, tempChar);
        cout << "Please enter the " << i + 1 << " slag: ";
        cin >> pt[i].slag;
        cin.get();
    }

    for (int i = 0; i < 2; i++)
    {
        cout << pt[i].dross << ": " << pt[i].slag << endl;
    }
    delete [] buffer;
    return 0;
}