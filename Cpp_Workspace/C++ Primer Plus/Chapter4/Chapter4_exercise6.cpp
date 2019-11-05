// 4.13.6 -- Array of CandyBar structure
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

    CandyBar snacks[3];
    snacks[0] = {"Brand_A", 2.3, 350};
    snacks[1] = {"Brand_B", 3.4, 450};
    snacks[2] = {"Brand_C", 4.5, 550};

    cout << snacks[0].brand << " has " << snacks[0].weight << " grams and " << snacks[0].carlore << " carlore." << endl;
    cout << snacks[1].brand << " has " << snacks[1].weight << " grams and " << snacks[1].carlore << " carlore." << endl;
    cout << snacks[2].brand << " has " << snacks[2].weight << " grams and " << snacks[2].carlore << " carlore." << endl;

    return 0;
}