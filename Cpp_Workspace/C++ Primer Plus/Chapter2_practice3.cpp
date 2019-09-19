// 2.7.3 -- calling user functions twice
#include <iostream>
#include <cmath>

using namespace std;

void usrfunc1(void);
void usrfunc2(void);

int main()
{
    usrfunc1();
    usrfunc1();
    usrfunc2();
    usrfunc2();

    return 0;
}

void usrfunc1()
{
    cout << "Three blind mice" << endl;
}

void usrfunc2()
{
    cout << "See how they run" << endl;
}
