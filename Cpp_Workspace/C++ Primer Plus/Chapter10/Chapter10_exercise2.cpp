// 10.10.2 -- Person class definitions
#include <iostream>
#include <string>
#include <cstring>
#include "Chapter10_exercise2.h"

Person::Person(const std::string& ln, const char* fn)
{
    lname = ln;
    std::strcpy(fname, fn);
}

void Person::Show() const
{
    std::cout << "Bonjour! " << fname << ' ' << lname;
}

void Person::FormalShow() const
{
    std::cout << "Bonjour! " << lname << ", " << fname;
}