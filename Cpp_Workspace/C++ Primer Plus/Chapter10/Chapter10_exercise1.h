// 10.10.1 -- class for bank accounts
#ifndef BANK_ACCOUNT_H_
#define BANK_ACCOUNT_H_
#include <string>
class BankAccount
{
    private:
        std::string name;
        std::string accountNo;
        double balance;
    public:
        BankAccount();
        BankAccount(std::string ne, std::string acct, double bal);
        void showAccount() const;
        void deposit(double cash);
        void withdraw(double cash);
};

#endif