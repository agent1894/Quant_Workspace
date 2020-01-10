// 10.10.3 -- main program for golf
#include <iostream>
#include "Chapter10_exercise3.golf.h"

int main()
{
    Golf golf1("Tiger", 5);
    golf1.showgolf();
    golf1.sethandicap(3);
    Golf golf2;
    golf2.showgolf();
    golf2.setgolf(golf2);
    golf2.showgolf();
    std::cout << "***** Official Solution *****" << std::endl;
    Golf golf3;
    golf3.setgolfOfficial();
    golf3.showgolf();
    return 0;
}