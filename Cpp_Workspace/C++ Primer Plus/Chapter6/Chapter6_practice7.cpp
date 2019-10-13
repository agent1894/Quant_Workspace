// 6.11.7 -- vowels and consonants
#include <iostream>
#include <cctype>
#include <string>

int main()
{
    using namespace std;
    cout << "Enter words (q to quit): " << endl;
    string input;
    cin >> input;
    int vowels = 0; 
    int consonants = 0; 
    int others = 0;
    while (input != "q")
    {
        if (isalpha(input[0]))
        {
            switch (input[0])
            {
                case 'a' :
                case 'A' :
                case 'e' :
                case 'E' : 
                case 'i' :
                case 'I' :
                case 'o' :
                case 'O' : 
                case 'u' :
                case 'U' :
                    vowels++;
                    break;
                default :
                    consonants++;
            }
        }
        else
            others++;
        cin >> input;
    }
    cout << vowels << " words beginning with vowels" << endl;
    cout << consonants << " words beginning with consonants" << endl;
    cout << others << " others" << endl;

    return 0;
}