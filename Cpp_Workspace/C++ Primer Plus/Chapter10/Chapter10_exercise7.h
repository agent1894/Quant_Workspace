// 10.10.7 -- class definition for the Betelgeusean plorg
#ifndef PLORG_H_
#define PLORG_H_
#include <cstring>

class Plorg
{
    private:
        char name[20];
        int CI;
    public:
        Plorg()
        {
            std::strcpy(name, "Plorga");
            CI = 50;
        }
        Plorg(const char ar[], int ci = 50);
        void changeCI(int ci);
        void showData() const;
};

#endif