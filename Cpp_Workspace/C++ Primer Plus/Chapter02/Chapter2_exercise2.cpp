// 2.7.2 -- convert long to yards
#include <iostream>

int main()
{
    using namespace std;
    cout << "Enter the distance in long: ";
    int distance;
    cin >> distance;
    cout << "The conversion of long is " << distance * 220 << " yards." << endl;

    return 0;
}