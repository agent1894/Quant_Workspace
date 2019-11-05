// 4.13.9 -- CandyBar using new
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

    CandyBar * pt = new CandyBar;
    pt->brand = "Brand_A";
    pt->weight = 2.3;
    pt->carlore = 350;
    cout << pt->brand << " has " << pt->weight << " grams and " << pt-> carlore << " carlore." << endl;
    
    pt->brand = "Brand_B";
    pt->weight = 3.4;
    pt->carlore = 450;
    cout << pt->brand << " has " << pt->weight << " grams and " << pt-> carlore << " carlore." << endl;

    pt->brand = "Brand_C";
    pt->weight = 4.5;
    pt->carlore = 550;
    cout << pt->brand << " has " << pt->weight << " grams and " << pt-> carlore << " carlore." << endl;

    delete pt;

    return 0;
}

