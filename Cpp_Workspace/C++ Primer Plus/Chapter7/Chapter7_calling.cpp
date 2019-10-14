// calling.cpp -- defining, prototyping, and calling a function
#include <iostream>

void simple(); // function prototype

int main()
{
    using namespace std;
    cout << "main() will call the simple() function: " << endl;
    simple(); // function call
    cout << "main() is finished with the simple() function. " << endl;
    // cin.get();
    return 0;
}

void simple()
{
    using namespace std;
    cout << "I'm but a simple function. " << endl;
}