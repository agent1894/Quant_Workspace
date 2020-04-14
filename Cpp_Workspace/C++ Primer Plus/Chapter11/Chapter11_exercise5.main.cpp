#include <iostream>
#include "Chapter11_exercise5.h"

int main()
{
    Stonewt wolfe = 285.7; // same as Stonewt wolfe(285.7)
    Stonewt taft(21, 8);

    std::cout << "wolfe: " << wolfe << std::endl;
    wolfe.set_stone();
    std::cout << "wolfe: " << wolfe << std::endl;
    std::cout << "taft: " << taft << std::endl;
    taft.set_float();
    std::cout << "taft: " << taft << std::endl;

    std::cout << "Now the sum: " << std::endl;
    Stonewt cal;
    cal = wolfe + taft;
    cal.set_int();
    std::cout << cal << std::endl;

    std::cout << "Now the diff: " << std::endl;
    cal = wolfe - taft;
    std::cout << cal << std::endl;

    std::cout << "Now the times: (taft * 4.2) " << std::endl;
    cal = taft * 4.2;
    cal.set_stone();
    std::cout << cal << std::endl;

    std::cout << "Try to use friend functions (4.2 * wolfe) " << std::endl;
    cal = 4.2 * wolfe;
    std::cout << cal << std::endl;
    cal.set_stone();
    std::cout << cal << std::endl;
    cal.set_int();
    std::cout << cal << std::endl;

    return 0;
}