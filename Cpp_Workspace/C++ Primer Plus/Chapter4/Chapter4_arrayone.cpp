// arrayone.cpp -- small arrays of integers
#include <iostream>
int main()
{
    using namespace std;

    int yams[3]; // create array with 3 elements
    yams[0] = 7;
    yams[1] = 8;
    yams[2] = 6;

    int yamcosts[3] = {20, 30 ,5}; // create and initialize array
    // 如果initialize无法通过编译，将int yamcosts[3]变为static int yamcosts[3]，应该是不同编译器产生的区别

    cout << "Total yams = ";
    cout << yams[0] + yams[1] + yams[2] << endl;
    cout << "The package with " << yams[1] << " yams costs ";
    cout << yamcosts[1] << " cents per yam." << endl;

    int total = yams[0] * yamcosts[0] + yams[1] * yamcosts[1];
    total = total + yams[2] * yamcosts[2];
    cout << "The total yams expenses is " << total << " cents." << endl;

    cout << "\nSize of yams array = " << sizeof(yams);
    cout << " bytes." << endl;
    cout << "Size of one element = " << sizeof(yams[0]);
    cout << " bytes." << endl;

    return 0;
}