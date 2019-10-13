// 6.11.1 -- read input until @
#include <iostream>
#include <cctype>

int main()
{
    using namespace std;
    char input;
    cout << "Enter characters; enter @ to quit. " << endl;
    while (cin.get(input))
    {
        if (input == '@')
            break;
        else if (!isalpha(input))
            continue;
        else if (islower(input))
            input = toupper(input);
        else
            input = tolower(input);
        cout << input;
    }

    return 0;
}