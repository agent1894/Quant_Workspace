#include <iostream>
#include <cstring>
#include "Chapter10_exercise3.golf.h"

Golf::Golf(const char* fn, int hc)
{
    std::strcpy(fullName, fn);
    handicap = hc;
}

Golf& Golf::setgolf(Golf& g)
{
    std::cout << "Enter the fullname of user: " << std::endl;
    char name[Len];
    std::cin.getline(name, Len);
    if (name[0] != '\0')
    {
        std::strcpy(this->fullName, name);
        std::cout << "Enter the handicap: " << std::endl;
        std::cin >> this->handicap;
        std::cin.get();
    }
    return *this;
}

int Golf::setgolfOfficial()
{
    std::cout << "Enter the fullname of user: " << std::endl;
    char name[Len];
    std::cin.getline(name, Len);
    if (name[0] != '\0')
    {
        std::cout << "Enter the handicap: " << std::endl;
        int hc;
        std::cin >> hc;
        *this = Golf(name, hc);
        std::cin.get();
        return 1;
    }
    else
    {
        return 0;
    }
}

void Golf::sethandicap(int hc)
{
    handicap = hc;
}

void Golf::showgolf() const
{
    std::cout << "The fullname of user is: " << fullName << std::endl;
    std::cout << "The handicap is: " << handicap << std::endl;
}