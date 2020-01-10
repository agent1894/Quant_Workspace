// 10.10.1 -- definition for BankAccount class functions
#include <iostream>
#include "Chapter10_exercise1.h"

BankAccount::BankAccount()
{
    name = "Empty User";
    accountNo = "00000000";
    balance = 0.0; 
} 

BankAccount::BankAccount(std::string ne, std::string acct, double bal)
{
    name = ne;
    accountNo = acct;
    balance = bal;
}

void BankAccount::showAccount() const
{
    std::cout << "This bank account belongs to " << name << std::endl;
    std::cout << "The account number is " << accountNo << " and the balance is $" << balance << std::endl;
}

void BankAccount::deposit(double cash)
{
    if (cash < 0.0)
    {
        std::cout << "You can not deposit negative cash amount!" << std::endl;
        std::cout << "Transaction is aborted." << std::endl;
    }
    else
    {
        balance += cash;
    }
}

void BankAccount::withdraw(double cash)
{
    if (cash < 0.0)
    {
        std::cout << "You can not withdraw negative cash amount!" << std::endl;
        std::cout << "Transaction is aborted." << std::endl;
    }
    else if (cash > balance)
    {
        std::cout << "You can not withdraw greater than balance you had!" << std::endl;
        std::cout << "Transaction is aborted." << std::endl;
    }
    else
    {
        balance -= cash;
    }
}