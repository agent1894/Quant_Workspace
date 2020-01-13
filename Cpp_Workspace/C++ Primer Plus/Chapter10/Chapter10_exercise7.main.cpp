// 10.10.7 -- main function to test Betelgeusean Plorg class
#include "Chapter10_exercise7.h"

int main()
{
    Plorg plorg1;
    plorg1.showData();
    Plorg plorg2("Betelgeusean");
    plorg2.showData();
    plorg2.changeCI(80);
    plorg2.showData();

    return 0;
}