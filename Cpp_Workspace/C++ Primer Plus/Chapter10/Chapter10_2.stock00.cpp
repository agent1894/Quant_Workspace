// stock00.cpp -- implementing the Stock class
// version 00
#include <iostream>
#include "Chapter10_1.stock00.h"

void Stock::acquire(const std::string& co, long n, double pr)
{
    company = co;
    if (n < 0)
    {
        std::cout << "Number of shares can't be negative; ";
        std::cout << company << " shares set to 0.\n";
        shares = 0;
    }
    else
    {
        shares = n;
    }
    share_val = pr;
    set_tot();
}

void Stock::buy(long num, double price)
{
    if (num < 0)
    {
        std::cout << "Number of shares purchased can't be negative. ";
        std::cout << "Transaction is aborted.\n";
    }
    else
    {
        shares += num;
        share_val = price;
        set_tot();
    }
}

void Stock::sell(long num, double price)
{
    using std::cout;
    if (num < 0)
    {
        cout << "Number of shares purchased can't be negative. ";
        cout << "Transaction is aborted.\n";
    }
    else if (num > shares)
    {
        cout << "Your can't sell more than you have! ";
        cout << "Transaction is aborted.\n";
    }
    else
    {
        shares -= num;
        share_val = price;
        set_tot();
    }
}

void Stock::update(double price)
{
    share_val = price;
    set_tot();
}

void Stock::show()
{
    using std::cout;
    using std::ios_base;
    // set format to #.###
    ios_base::fmtflags orig = cout.setf(ios_base::fixed, ios_base::floatfield);
    std::streamsize prec = cout.precision(3);
    std::cout << "Company: " << company;
    std::cout << " Shares: " << shares << '\n';
    std::cout << " Share Price: $" << share_val;
    // set format to #.##
    cout.precision(2);
    std::cout << " Total Worth: $" << total_val << '\n';
    // restore original format
    cout.setf(orig, ios_base::floatfield);
    cout.precision(prec);
}
