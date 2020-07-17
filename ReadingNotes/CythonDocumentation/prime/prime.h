#include <iostream>
#include <vector>
#include <chrono>
#include <unistd.h>
#include <time.h>

class PRIME
{
    public:
        PRIME();
        PRIME(unsigned int n);
        ~PRIME(){};
        void calculate();
        void show();
    private:
        std::vector<unsigned int> list;
        unsigned int num;
};
