// 10.10.6 -- main function to test the class
#include <iostream>
#include "Chapter10_exercise6.h"

int main()
{
    using namespace std;
    Move move1(1.1, 9.9);
    cout << "The move1 is:\n";
    move1.showmove();
    cout << "The move2 is:\n";
    Move move2 = move1.add(move1);
    move2.showmove();
    cout << "The move1.add(move2) is:\n";
    move1.add(move2).showmove();

    return 0;
}