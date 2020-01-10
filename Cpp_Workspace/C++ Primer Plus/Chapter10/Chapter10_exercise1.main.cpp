// 10.10.1 -- main program for bank account exercise
#include <iostream>
#include "Chapter10_exercise1.h"

int main()
{
    BankAccount accountEmpty;
    accountEmpty.showAccount();
    BankAccount account("Bruce Wayne", "TinyAccount01", 9876543.21);
    account.showAccount();
    account.deposit(-3.0);
    account.showAccount();
    account.deposit(1234567.89);
    account.showAccount();
    account.withdraw(-5.0);
    account.showAccount();
    account.withdraw(10000000.0);
    account.showAccount();
    account.withdraw(10000000.0);
    account.showAccount();
    return 0;
}