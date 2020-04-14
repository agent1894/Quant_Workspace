#include <iostream>
#include "Chapter11_exercise6.h"

int main()
{
    const int len = 6;
    Stonewt stonewtarr[len] = 
    {
        Stonewt(285.7),
        Stonewt(21, 8),
        Stonewt(218)
    };
    for (int i = 3; i < len; i++)
    {
        double pounds;
        std::cout << "Enter #" << i + 1 << " Stonewt weight (in pounds): ";
        if (std::cin >> pounds)
        {
            stonewtarr[i] = Stonewt(pounds);
        }
        else
        {
            std::cout << "Invalid weight, set to 0." << std::endl;
            stonewtarr[i] = Stonewt();
        }
    }
    const Stonewt compare(11, 0);
    Stonewt min = stonewtarr[0];
    Stonewt max = stonewtarr[0];
    int count = 0;
    for (int i = 0; i < len; i++)
    {
        if (stonewtarr[i] < min)
        {
            min = stonewtarr[i];
        }
        if (stonewtarr[i] > max)
        {
            max = stonewtarr[i];
        }
        if (stonewtarr[i] >= compare)
        {
            count++;
        }
    }
    std::cout << "The maximum weight is " << max << std::endl;
    std::cout << "The minimum weight is " << min << std::endl;
    std::cout << "The number of elements larger or equal to 11 stones is " << count << std::endl;

    return 0;
}