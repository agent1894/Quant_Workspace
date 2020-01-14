// 5.9.9 -- read single words by using string
#include <iostream>
#include <string>

int main()
{
    using namespace std;

    cout << "Enter words (to stop, type the word done): " << endl;
    string ch;
    int i = 0;
    do
    {
        cin >> ch;
        ++i;
    }
    while (ch != "done");

    cout << "You entered a total of " << i - 1 << " words." << endl;

    return 0;
}