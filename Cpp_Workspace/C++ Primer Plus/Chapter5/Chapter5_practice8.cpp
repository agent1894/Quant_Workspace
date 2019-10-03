// 5.9.8 -- read single words
#include <iostream>
#include <cstring>

int main()
{
    using namespace std;

    cout << "Enter words (to stop, type the word done): " << endl;
    char ch[80];
    int i = 0;
    do
    {
        cin >> ch;
        ++i;
    }
    while (strcmp(ch, "done") != 0);

    cout << "You entered a total of " << i - 1 << " words." << endl;

    return 0;
}