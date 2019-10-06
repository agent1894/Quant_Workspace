// cctypes.cpp -- using the ctype.h library
#include <iostream>
#include <cctype> // prototypes for character functions

int main()
{
    using namespace std;

    cout << "Enter text for analysis, and type @ to terminate input." << endl;
    char ch;
    int whitespace = 0;
    int digits = 0;
    int chars = 0;
    int punct = 0;
    int others = 0;

    cin.get(ch); // get first character
    while (ch != '@') // test for sentinel
    {
        if (isalpha(ch)) // is it an alphabetic character?
            chars++;
        else if (isspace(ch)) // is it a whitespace character?
            whitespace++;
        else if (isdigit(ch)) // is it a digit?
            digits++;
        else if (ispunct(ch)) // is it a punctuation?
            punct++;
        else
            others++;
        cin.get(ch); // get next character
    }

    cout << chars << " letters, ";
    cout << whitespace << " whitespace, ";
    cout << digits << " digits, ";
    cout << punct << " punctuations, ";
    cout << others << " others." << endl;

    return 0;
}