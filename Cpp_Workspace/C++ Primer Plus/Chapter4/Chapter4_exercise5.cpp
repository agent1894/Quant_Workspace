// 4.13.5 -- CandyBar structure
#include <iostream>
#include <string>

struct CandyBar
{
    std::string brand;
    double weight;
    int carlore;
};

int main()
{
    using namespace std;

    CandyBar snack = {"Mocha Munch", 2.3, 350};
    cout << "The brand of snack is: " << snack.brand << endl;
    cout << "The weight of snack is: " << snack.weight << endl;
    cout << "The carlore of snack is: " << snack.carlore << endl;

    return 0;
}