// 7.13.4 -- lottery
#include <iostream>
long double probability(unsigned numbers, unsigned picks);

int main()
{
    using namespace std;
    cout << "Enter the field number and the picks (q to quit): " << endl;
    unsigned int field, picks, special;
    while ((cin >> field >> picks) && (picks < field))
    {
        cout << "Enter the special number: " << endl;
        if (cin >> special)
        {
            cout << "The winning probability of picking " << picks;
            cout << " from " << field << " numbers is one in: ";
            cout << probability(field, picks) << endl;
            cout << "The winning probability of picking one number from ";
            cout << special <<" numbers is one in ";
            cout << probability(special, 1) << endl;
            cout << "The probability of get the first prize is one in: ";
            cout << probability(field, picks) * probability(special, 1) << endl;
            cout << "Enter the field number and the picks (q to quit): " << endl;
        }
        else
            break;
    }

    return 0;
}

long double probability(unsigned numbers, unsigned picks)
{
    long double result = 1.0;
    long double n;
    unsigned p;

    for (n = numbers, p = picks; p > 0; n--, p--)
        result = result * n / p;
    return result;
}