// 9.6.1 -- function definitions
#include <iostream>
#include <cstring>
#include "Chapter9_exercise1.golf.h"


void setgolf(golf & g, const char * name, int hc)
{
    std::strcpy(g.fullname, name);
    g.handicap = hc;
}

int setgolf(golf & g)
{
    std::cout << "Enter the fullname of user: " << std::endl;
    char name[Len];
    std::cin.getline(name, Len);
    if (name[0] != '\0')
    {
        std::cout << "Enter the handicap: " << std::endl;
        int hc;
        std::cin >> hc;
        setgolf(g, name, hc);
        std::cin.get();
        return 1;
    }
    else
        return 0;
}

void handicap(golf & g, int hc)
{
    g.handicap = hc;
}

void showgolf(const golf & g)
{
    std::cout << "The fullname of user is: " << g.fullname << std::endl;
    std::cout << "The handicap is: " << g.handicap << std::endl;
}