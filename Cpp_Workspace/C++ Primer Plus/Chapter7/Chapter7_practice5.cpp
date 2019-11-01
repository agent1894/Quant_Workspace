// 7.13.5 -- recursion of factorials
#include <iostream>
unsigned long long factorial(unsigned int n);

int main()
{
    using namespace std;
    cout << "Enter an integer: ";
    unsigned int n;
    while (cin >> n)
    {
        cout << "The factorial of " << n << " is " << factorial(n) << endl;
        cout << "Enter an integer: ";
    }
    cout << "Done!" << endl;
    
    return 0;
}

unsigned long long factorial(unsigned int n)
{
    unsigned long long fac;
    if (n == 0)
        fac = 1;
    else
        fac = n * factorial(n - 1);
    return fac;
}